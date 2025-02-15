import pydash as _


from constants import TITLING


def filter_api(data):
    # Теперь если даже нет поля item (которое ранее отвечало за наличие), все равно добавляем такой товар.
    # if not _.get(data, "data.item", "-1") != "-1":
    #     return False

    for brandId in _.get(data, "data.detail.relationBrandIds", list()):
        if str(brandId) in TITLING:
            return True

    return str(_.get(data, "data.detail.brandId", -1)) in TITLING
