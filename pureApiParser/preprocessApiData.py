import copy

import pydash as _


def preprocess_dewu_api(unprocessed_data):
    d = dict()

    data = copy.deepcopy(unprocessed_data)

    #
    #

    d["images_full"] = list()
    images = _.get(data, 'data.image.spuImage.images', list())
    for image in images:
        if "desc" in image:
            del image["desc"]
        d["images_full"].append(image)

    d["images"] = list()
    for image_dict in d["images_full"]:
        if "url" in image_dict:
            d["images"].append(image_dict["url"])
    #
    d["arSkuIdRelation"] = list()
    arSkuIdRelations = _.get(data, 'data.image.spuImage.arSkuIdRelation', list())
    for arSkuIdRelation in arSkuIdRelations:
        if "supportFlag" in arSkuIdRelation:
            del arSkuIdRelation["supportFlag"]
        d["arSkuIdRelation"].append(arSkuIdRelation)
    #
    d["gif"] = _.get(data, "data.image.spuImage.threeDimension.gifUrl", "")

    #
    #

    d["poizonSpuGroupList"] = _.get(data, 'data.spuGroupList.list', list())
    for poizonSpuGroupListItem in d["poizonSpuGroupList"]:
        # if "logoUrl" in poizonSpuGroupListItem:
        #     del poizonSpuGroupListItem["logoUrl"]
        if "goodsType" in poizonSpuGroupListItem:
            del poizonSpuGroupListItem["goodsType"]
        if "title" in poizonSpuGroupListItem:
            del poizonSpuGroupListItem["title"]
        if "spu3d360ShowType" in poizonSpuGroupListItem:
            del poizonSpuGroupListItem["spu3d360ShowType"]

    #
    #

    d["spuId"] = _.get(data, "data.detail.spuId", 0)
    #
    d["brandId"] = _.get(data, "data.detail.brandId", 0)
    d["relatedBrands"] = _.get(data, "data.detail.relationBrandIds", list())
    d["allBrands"] = d["relatedBrands"]
    if d["brandId"]:
        d["allBrands"] = [d["brandId"]] + d["allBrands"]
    #
    d["title"] = " ".join(_.get(data, "data.detail.title", ""))
    #
    d["categoryId"] = _.get(data, "data.detail.categoryId", -1)
    d["categoryName"] = _.get(data, "data.detail.categoryName", "")
    d["level1CategoryId"] = _.get(data, "data.detail.level1CategoryId", -1)
    d["level2CategoryId"] = _.get(data, "data.detail.level2CategoryId", -1)
    #
    d["manufacturer_sku"] = _.get(data, "data.detail.articleNumber", "")
    skus = [_.get(data, "data.detail.articleNumber", ""), _.get(data, "data.detail.otherNumbers", "")] + _.get(data,
                                                                                                               "data.detail.articleNumbers",
                                                                                                               list())
    d["manufacturer_skus"] = [sku for sku in list(set(skus)) if sku]
    if not d["manufacturer_sku"] and d["manufacturer_skus"]:
        d["manufacturer_sku"] = d["manufacturer_skus"][0]

    if len(d["manufacturer_skus"]) <= 1:
        d["manufacturer_skus"] = []
    else:
        d["manufacturer_skus"] = d["manufacturer_skus"][1:]
    #
    d["releaseDate"] = _.get(data, "data.detail.sellDate", "")
    #
    d["retailPrice"] = _.get(data, "data.detail.authPrice", 0)
    #
    d["fitId"] = _.get(data, "data.detail.fitId", -1)
    #
    d["goodsType"] = _.get(data, "data.detail.goodsType", -1)
    d["subTitle"] = _.get(data, "data.detail.subTitle", "")
    d["description"] = _.get(data, "data.detail.desc", "")

    #
    #

    d["skus"] = _.get(data, "data.skus", list())

    #
    #

    d["item"] = _.get(data, "data.item", dict())

    #
    #

    d["likesCount"] = _.get(data, "data.favoriteCount.count", 0)
    d["parameters"] = _.get(data, "data.keyProperties", [])

    return d
