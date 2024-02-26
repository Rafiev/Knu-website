from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


user_post_swagger = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'username': openapi.Schema(type=openapi.TYPE_STRING),
                    'password': openapi.Schema(type=openapi.TYPE_STRING)},
        required=['username', 'password'],  
    ),
    responses={201: openapi.Response(description="", 
                                     examples={'application/json': {'msg': 'Вы успешно добавили пользователя'}}),
               400: openapi.Response(description=" ",
                                     examples={'application/json': {'msg': 'serializer.error'}})},
    operation_summary="Добавление пользователя",
    operation_description="Этот эндпоинт используется для добавления нового пользователя.")

user_delete_swagger = swagger_auto_schema(
    operation_summary="Удаление абитуриента",
    operation_description="Этот эндпоинт удаляет абитуриента по его идентификатору.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'username': openapi.Schema(type=openapi.TYPE_STRING)},
        required=['username']),
    responses={
        204: openapi.Response(description="", examples={"application/json": {"msg": "Пользователь успешно удален"}}),
        404: openapi.Response(description="", examples={"application/json": {"msg": "Пользователь не найден"}}),
        405: openapi.Response(description="", examples={"application/json": {"msg": "У вас недостаточный уровень доступа"}})
    }
)