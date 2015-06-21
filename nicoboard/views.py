# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from rest_framework import permissions, routers, serializers, viewsets
from kombu import BrokerConnection, Exchange, Producer

from nicoboard.models import Board, Message
# Create your views here.

conn = BrokerConnection(hostname='127.0.0.1',
                        port=5672,
                        userid='guest',
                        password='guest',
                        virtual_host='/')

ex = Exchange("amq.topic", "topic")





class BoardSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username",
                                         read_only=True,
                                         default=serializers.CurrentUserDefault())
    class Meta:
        model = Board
        fields = ('id', 'name','owner', 'created_at', 'modified_at')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    board = serializers.SlugRelatedField(slug_field="name",
                                         queryset=Board.objects.all(),
                                         default=serializers.CreateOnlyDefault(1))
    owner = serializers.SlugRelatedField(slug_field="username",
                                         read_only=True,

                                         default=serializers.CurrentUserDefault())
    class Meta:
        model = Message
        fields = ('id', 'url', 'board','body','owner', 'created_at', 'modified_at')

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
#    permission_classes = [permissions.IsAdminUser]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BoardViewSet, self).dispatch(*args, **kwargs)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(MessageViewSet, self).dispatch(*args, **kwargs)

    def create(self, request):
        ch = conn.channel()
        producer = Producer(ch, ex, "hackday")
        producer.publish("test")
        return super(MessageViewSet, self).create(request);

class BoardDetailView(DetailView):
    model = Board
    slug_field = "name"


    def get_context_data(self, **kwargs):
        # コンテキストを取得するために、先に基底クラスの機能を呼び出します。
        context = super(BoardDetailView, self).get_context_data(**kwargs)
        # 全書籍のクエリセットを追加します。
        context['message_list'] = self.object.message_set.order_by("-created_at")[:100]
        return context

class MonitorDetailView(DetailView):
    model = Board
    slug_field = "name"
    template_name = "nicoboard/monitor_detail.html"
