from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


applicant_post_swagger = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'created_at': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
                    'grade': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING)},
        required=['grade', 'name', 'phone_number'],  
    ),
    responses={201: openapi.Response(description="", 
                                     examples={'application/json': {'msg': 'Абитуриент успешно создан'}}),
               400: openapi.Response(description=" ",
                                     examples={'application/json': {'msg': 'serializer.error'}})},
    operation_summary="Добавление абитуриента",
    operation_description="Этот эндпоинт используется для добавления нового абитуриента.")


applicant_get_swagger = swagger_auto_schema(
    operation_summary="Получение списка абитуриентов",
    operation_description="Этот эндпоинт возвращает список абитуриентов",
    responses={200: openapi.Response(description="",
                                     examples={"application/json": [{"id": 1, 
                                                                     "created_at": "2024-02-04",
                                                                     "name": "Рафиев Эмирлан",
                                                                     "grade": 9,
                                                                     "phone_number": '0551106750'},
                                                                    {"id": 2, 
                                                                     "created_at": "2024-02-04",
                                                                     "name": "Осмонов Аскат",
                                                                     "grade": 11,
                                                                     "phone_number": '0551106750'},]})})



applicant_delete_swagger = swagger_auto_schema(
    operation_summary="Удаление абитуриента",
    operation_description="Этот эндпоинт удаляет абитуриента по его идентификатору.",
    responses={
        204: openapi.Response(description="", examples={"application/json": {"msg": "Объект успешно удален"}}),
        404: openapi.Response(description="", examples={"application/json": {"msg": "Объект не найден"}})
    }
)