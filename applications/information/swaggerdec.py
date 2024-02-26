from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


compound_post_swagger = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'position': openapi.Schema(type=openapi.TYPE_STRING),
                    'description': openapi.Schema(type=openapi.TYPE_STRING),
                    'image': openapi.Schema(type=openapi.TYPE_FILE)},
        required=['position', 'name', 'description', 'image',],  
    ),
    responses={201: openapi.Response(description="", 
                                     examples={'application/json': {'msg': 'Сотрудник успешно создан'}}),
               400: openapi.Response(description=" ",
                                     examples={'application/json': {'msg': 'serializer.error'}})},
    operation_summary="Добавление сотрудника",
    operation_description="Этот эндпоинт используется для добавления нового сотрудника.")


compound_get_swagger = swagger_auto_schema(
    operation_summary="Получение списка сотрудников",
    operation_description="Этот эндпоинт возвращает список сотрудников",
    responses={200: openapi.Response(description="",
                                     examples={"application/json": [{"id": 1,
                                                                    "name": "Аса Акира",
                                                                    "position": "Менеджер",
                                                                    "image": "/media/images/2c241856cc258ed48bdff0555adfd140.jpg"},
                                                                    {"id": 2,
                                                                     "name": "Осмонов Аскат",
                                                                     "position": "Директор",
                                                                     "image": "/media/images/2c241856cc258ed48bdff0555adfd140.jpg"},]})})



compound_get_detail_swagger = swagger_auto_schema(
    operation_summary="Получение деталей сотрудника",
    operation_description="Этот эндпоинт возвращает детали сотрудника по ее идентификатору.",
    responses={200: openapi.Response(description="", schema=openapi.Schema(type=openapi.TYPE_OBJECT,
            properties={'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'position': openapi.Schema(type=openapi.TYPE_STRING),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),
                        'image': openapi.Schema(type=openapi.TYPE_FILE)})),
               404: openapi.Response(description="", examples={"application/json": {"msg": "Сотрудник не найден"}})})


compound_delete_swagger = swagger_auto_schema(
    operation_summary="Удаление сотрудника",
    operation_description="Этот эндпоинт удаляет сотрудника по его идентификатору.",
    responses={
        204: openapi.Response(description="", examples={"application/json": {"msg": "Объект успешно удален"}}),
        404: openapi.Response(description="", examples={"application/json": {"msg": "Объект не найден"}})
    }
)

new_post_swagger = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'title': openapi.Schema(type=openapi.TYPE_STRING),
                    'description': openapi.Schema(type=openapi.TYPE_STRING),
                    'image': openapi.Schema(type=openapi.TYPE_FILE),
                    'image': openapi.Schema(type=openapi.TYPE_FILE),},
        required=['name', 'description', 'image', 'image'],  
    ),
    responses={201: openapi.Response(description="", 
                                     examples={'application/json': {'msg': 'Новость успешно создана'}}),
               400: openapi.Response(description=" ",
                                     examples={'application/json': {'msg': 'serializer.error'}})},
    operation_summary="Добавление новости",
    operation_description="Этот эндпоинт используется для добавления новости.")


new_get_swagger = swagger_auto_schema(
    operation_summary="Получение списка новостей",
    operation_description="Этот эндпоинт возвращает список новостей",
    responses={200: openapi.Response(description="",
                                     examples={"application/json": [{"id": 1,
                                                                     "title": "Сказка",
                                                                     "created_at": "2024-02-26"
                                                                     },
                                                                    {"id": 1,
                                                                     "title": "Сказка",
                                                                     "created_at": "2024-02-26"
                                                                     }]})})

new_get_detail_swagger = swagger_auto_schema(
    operation_summary="Получение деталей новости",
    operation_description="Этот эндпоинт возвращает детали новости по ее идентификатору.",
    responses={404: openapi.Response(description="", examples={"application/json": {"msg": "Сотрудник не найден"}}),
               200: openapi.Response(description="",
                                     examples={"application/json": {"id": 1,
                                                                    "images": [
                                                                        "/media/images/1667331596_34-celes-club-p-van-pis-oboi-na-rabochii-stol-vkontakte-34.jpg",
                                                                        "/media/images/3572335ba261b909e7c170fd32389217.jpg"],
                                                                    "created_at": "2024-02-26",
                                                                    "title": "Сказка",
                                                                    "description": "sfgsdgsdfgsdgdgs" }})})


new_delete_swagger = swagger_auto_schema(
    operation_summary="Удаление новости",
    operation_description="Этот эндпоинт удаляет новость по ее идентификатору.",
    responses={
        204: openapi.Response(description="", examples={"application/json": {"msg": "Объект успешно удален"}}),
        404: openapi.Response(description="", examples={"application/json": {"msg": "Объект не найден"}})
    }
)