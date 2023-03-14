
import json


class Bolt_order_info:
    def __init__(self , order: dict, organizationId, terminalGroupId, orderTypeId, paymentTypeId ) -> None:
        self.order = order
        self.provider_id = order["provider_id"]
        self.order_id = order["order_id"]
        self.order_reference_id = order["order_reference_id"]
        self.pag_laikas = order["due_datetime"]
        self.order_kaina = order["total_order_price"]["value"]
        self.order_komentaras = order["user_note"]
        self.organizationId = organizationId
        self.terminalGroupId = terminalGroupId
        self.orderTypeId = orderTypeId
        self.customer_name = order["customer"]["partial_name"]
        self.paymentTypeId = paymentTypeId


    def bolt_patiekalai(self):
        self.bolt_patiekalu_info = self.order["items"]
        return self.bolt_patiekalu_info
    def order_header(self):


        order_info = {
            "organizationId":self.organizationId,
            "terminalGroupId":self.terminalGroupId,
            "createOrderSettings":{
            "transportToFrontTimeout":0
            },
            "order":{
            "comment": f"#{self.order_reference_id} , {self.order_komentaras}",
            "id": "null",
            "completeBefore": self.pag_laikas,
            "phone": "+37061111111",
            "orderTypeId": self.orderTypeId,
            "orderServiceType": "null",
            "customer":{
                "id": "null",
                "name": f"BOLT užsakymas: {self.customer_name}"
                        },
            "items": [],
            "payments":[
         {
            "paymentTypeKind": "Card",
            "sum": self.order_kaina,
            "paymentTypeId": self.paymentTypeId,
            "isProcessedExternally": "false"
         }
      ]
        }
    }
        

        return order_info



iiko_pradzia = {
   "organizationId":"b0cf0635-fe93-4911-b17f-b38d0248498a",
   "terminalGroupId":"a55741f7-0f8d-4acc-a4fa-445087666e50",
   "createOrderSettings":{
      "transportToFrontTimeout":0
   },
}
b_order = {
   "provider_id":"2nhVJNvJyF",
   "order_id":107472754,
   "order_reference_id":"8MK0A",
   "order_type":"delivery",
   "payment_type":"card_online",
   "created_ts":1677610377,
   "created_datetime":"2023-03-01T06:52:57.522+12:00",
   "due_ts":1677610448,
   "due_datetime":"2023-03-01T06:54:08.522+12:00",
   "customer":{
      "user_id":"b3e772c2-8d65-46cb-84a0-ff114d7c3630",
      "partial_name":"Danielius A.",
      "partial_phone":"********2323",
      "address_info":{
         
      }
   },
   "items":[
      {
         "name":"Sumustinis",
         "sku":"132",
         "qty":1,
         "unit_item_price":{
            "value":0.1,
            "currency":"eur"
         },
         "options":[
            {
               "name":"Keciupas",
               "sku":"1456",
               "qty":1,
               "unit_item_price":{
                  "value":0,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":0,
                  "currency":"eur"
               }
            },
            {
               "name":"Pakuote 2 privaloma",
               "sku":"55566",
               "qty":1,
               "unit_item_price":{
                  "value":0.5,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":0.5,
                  "currency":"eur"
               }
            }
         ],
         "total_item_price":{
            "value":0.6,
            "currency":"eur"
         }
      },
      {
         "name":"Burger",
         "sku":"14441",
         "qty":1,
         "unit_item_price":{
            "value":10,
            "currency":"eur"
         },
         "options":[
            {
               "name":"Milinda",
               "sku":"1171819",
               "qty":1,
               "unit_item_price":{
                  "value":4,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":4,
                  "currency":"eur"
               }
            },
            {
               "name":"Keciupas",
               "sku":"1456",
               "qty":1,
               "unit_item_price":{
                  "value":0,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":0,
                  "currency":"eur"
               }
            },
            {
               "name":"Pakuote 2 privaloma",
               "sku":"55566",
               "qty":1,
               "unit_item_price":{
                  "value":0.5,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":0.5,
                  "currency":"eur"
               }
            }
         ],
         "total_item_price":{
            "value":14.5,
            "currency":"eur"
         }
      },
      {
         "name":"Bulvytės fry",
         "sku":"123456",
         "qty":1,
         "unit_item_price":{
            "value":0.11,
            "currency":"eur"
         },
         "options":[
            {
               "name":"Milinda",
               "sku":"1171819",
               "qty":1,
               "unit_item_price":{
                  "value":4,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":4,
                  "currency":"eur"
               }
            },
            {
               "name":"Fanta",
               "sku":"6993",
               "qty":1,
               "unit_item_price":{
                  "value":2,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":2,
                  "currency":"eur"
               }
            },
            {
               "name":"BBQ",
               "sku":"963",
               "qty":1,
               "unit_item_price":{
                  "value":0,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":0,
                  "currency":"eur"
               }
            },
            {
               "name":"Pakuote 2 privaloma",
               "sku":"55566",
               "qty":1,
               "unit_item_price":{
                  "value":0.5,
                  "currency":"eur"
               },
               "total_item_price":{
                  "value":0.5,
                  "currency":"eur"
               }
            }
         ],
         "total_item_price":{
            "value":6.61,
            "currency":"eur"
         },
         "user_note":"Komentaras virtuve"
      }
   ],
   "total_order_price":{
      "value":21.71,
      "currency":"eur"
   },
   "user_note":"Komentaras bendras"
}
organizationId = "b0cf0635-fe93-4911-b17f-b38d0248498a"
terminalGroupId = "a55741f7-0f8d-4acc-a4fa-445087666e50"
orderTypeId = "68eec667-cb1e-4a9a-93c2-32cbfcfd259e"
paymentTypeId = "ee8ad1fc-ae0b-49e9-b17f-bedf86699dfa"

bolt_order = Bolt_order_info(b_order, organizationId, terminalGroupId, orderTypeId, paymentTypeId)

iiko_order_be_patiekalu = bolt_order.order_header()

bolt_patiekalu_informacija = bolt_order.bolt_patiekalai()




class Bolt_patiekalu_info:
    def __init__(self, patiekalai_bolt) -> None:
        try:
            self.name = patiekalai_bolt["name"]
            self.sku = patiekalai_bolt["sku"]
            self.kiekis = patiekalai_bolt["qty"]
            self.patiekalo_kaina = patiekalai_bolt["unit_item_price"]["value"]
            self.patiekalo_modifikatoriai = patiekalai_bolt["options"]
            self.patiekalo_komentaras = patiekalai_bolt["user_note"]
        except Exception as e:
            print(f"REIKIA LOGINTI: {e}")

        self.iiko_meniu = {
    "correlationId": "985295d8-f559-4361-b3da-6c781df3a43f",
    "groups": [
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 11,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "dc3f2bc5-8c73-424c-88f8-7fecebe6b1ee",
            "code": "",
            "name": "Sirupai",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 10,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "173989e7-f9b8-498f-b9ca-c8d6740548a9",
            "code": "",
            "name": "Service fee",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 9,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "f7a5388d-b4ca-4e1f-8bb3-b61584be04e2",
            "code": "",
            "name": "salotos",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 8,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "08b64dde-359a-4dae-818e-4516b67403ad",
            "code": "",
            "name": "Pak",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 7,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "9864986e-ac81-4aa8-9223-f3d5e3b26436",
            "code": "",
            "name": "padazai",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 6,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "cf243fe6-6818-4ada-90c4-507a1e7a947d",
            "code": "",
            "name": "Kepiniai",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 5,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "207715eb-fdfd-496c-b144-c1246e8e3454",
            "code": "",
            "name": "Kava",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 4,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "ff1a76ca-715c-4151-967f-4187f29c37e8",
            "code": "",
            "name": "GUACAMOLE",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "ff1a76ca-715c-4151-967f-4187f29c37e8",
            "order": 3,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "ed2068fd-26df-448c-9b3f-848eec6f0f5e",
            "code": "",
            "name": "Vaikiškas meniu\\Children's men",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "ed2068fd-26df-448c-9b3f-848eec6f0f5e",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "5f61abe5-fecf-4ea0-8ac8-78971c0eeddb",
            "code": "",
            "name": "Pagrindiniai pat. VM\\main dish",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "ff1a76ca-715c-4151-967f-4187f29c37e8",
            "order": 2,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "c3ec88b8-9cc7-4f71-a016-6a9006c480ac",
            "code": "",
            "name": "Nachos\\FILLED NACHOS BAKED WIT",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "ff1a76ca-715c-4151-967f-4187f29c37e8",
            "order": 1,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "3cf42853-477e-46ef-925a-f06a8acefae7",
            "code": "",
            "name": "Enchiladas\\ENCHILADA",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "ff1a76ca-715c-4151-967f-4187f29c37e8",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "372a009f-cd33-40b3-a9ac-034f1be4268e",
            "code": "",
            "name": "Desertai\\Desserts",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 3,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "61c5dc04-b2f1-450d-9b89-d5b6df8e5c8b",
            "code": "",
            "name": "gaivieji ger",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 2,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "25c1ac5f-1ef3-44c0-acac-cbf3ee2dbcbb",
            "code": "",
            "name": "Bendi",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 1,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "10a410d9-0416-497c-959a-398fd2287d09",
            "code": "",
            "name": "SASHIMI",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "false",
            "id": "7a4dbc8d-00c3-487a-866d-a06db8f2a8df",
            "code": "",
            "name": "SUSHI",
            "description": "null",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "true",
            "id": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "code": "12",
            "name": "Sirupai",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "true",
            "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
            "code": "66",
            "name": "Bendi",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "true",
            "id": "06119ba2-0def-4138-bd09-d3142b0070ea",
            "code": "24",
            "name": "salotos",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "true",
            "id": "e1680e45-c334-425f-8b62-acedfd4357ac",
            "code": "22",
            "name": "gaivieji ger",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "imageLinks": [],
            "parentGroup": "null",
            "order": 0,
            "isIncludedInMenu": "true",
            "isGroupModifier": "true",
            "id": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "code": "34",
            "name": "padazai",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        }
    ],
    "productCategories": [
        {
            "id": "0f598026-aabf-4a95-0186-415a50d66f0e",
            "name": "baras",
            "isDeleted": "false"
        },
        {
            "id": "0f598026-aabf-4a95-0186-415a50d66f0d",
            "name": "Kepiniai",
            "isDeleted": "false"
        },
        {
            "id": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "name": "virtuve",
            "isDeleted": "false"
        }
    ],
    "products": [
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "af72b438-2a70-4e2d-b71a-04ada1f4736b",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "08b64dde-359a-4dae-818e-4516b67403ad",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
            "code": "015",
            "name": "015",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "083a2f96-5657-4204-b3f7-2fbd21a0824b",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0d",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 1.500000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "cf243fe6-6818-4ada-90c4-507a1e7a947d",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "f01444cb-6b22-4315-a377-be3ddb377519",
            "code": "00008",
            "name": "Bulkutė su varške",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "083a2f96-5657-4204-b3f7-2fbd21a0824b",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0d",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 1.800000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "cf243fe6-6818-4ada-90c4-507a1e7a947d",
            "order": 1,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "f618f661-ec6f-4a0a-8b6d-b8ae545dfad4",
            "code": "00009",
            "name": "Bulkutė su obuoliais",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "083a2f96-5657-4204-b3f7-2fbd21a0824b",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0d",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 1.500000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "cf243fe6-6818-4ada-90c4-507a1e7a947d",
            "order": 2,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "e7ea3e61-5052-4a00-8f7d-2ec7ef02906d",
            "code": "00007",
            "name": "Bulkutė su džemu",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "beac09f7-05ec-4c9b-814b-14db36baaf66",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0e",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 2.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [
                {
                    "id": "a74be7cf-ace9-4036-9571-71db5457bd3d",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "c790e296-50db-4a3b-acc4-8a85c3dadbf2",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "c1a6e1b1-ec1d-44aa-b820-988ebb733dd3",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "1266420a-0171-4a88-8356-e346d0ba90a7",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "9ce2fb04-077c-4e1a-9c2e-f5683aca8d15",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "207715eb-fdfd-496c-b144-c1246e8e3454",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "4faccf33-6936-4c48-afd5-b547e74a3e7f",
            "code": "00006",
            "name": "Kava su pienu",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "beac09f7-05ec-4c9b-814b-14db36baaf66",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0e",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 1.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "207715eb-fdfd-496c-b144-c1246e8e3454",
            "order": 1,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "55c8f5fb-6f78-49a3-bdfc-60161517b26b",
            "code": "00005",
            "name": "Kava 1eur",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "13f7b8ae-05d2-48e5-9de8-e0c7f65eb077",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "5f61abe5-fecf-4ea0-8ac8-78971c0eeddb",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "66a38f02-3afc-4dda-a92e-74f62b06b245",
            "code": "922.0",
            "name": "922.0",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "5471c05b-38d7-43cd-857b-5bf26160846f",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "c3ec88b8-9cc7-4f71-a016-6a9006c480ac",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "6b410772-a53f-4d28-b749-501cb5b92425",
            "code": "323.0",
            "name": "323.0",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "22273e2a-1c45-4309-a257-d39ffc076bec",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "3cf42853-477e-46ef-925a-f06a8acefae7",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "cc239504-c9b6-4f43-9f5b-02163e1464bb",
            "code": "332.0",
            "name": "332.0",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "d8710316-f5aa-496c-b863-fdb49c9104b8",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "372a009f-cd33-40b3-a9ac-034f1be4268e",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "c72e575d-9312-4d52-94b5-4cf6d351e36b",
            "code": "2683.0",
            "name": "2683.0",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "56a1b8c0-326d-4d4a-b3e1-bcbc8831ad9e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 99,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 12,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "5dfa18b8-9dcf-4056-81c0-c40efdbe3e94",
            "code": "3736105",
            "name": "WOLT NERA",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 13.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "3b8a8ffe-ea6e-41d4-86df-f159809585a8",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "06119ba2-0def-4138-bd09-d3142b0070ea",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "864653b0-dd39-4f74-9a3b-dd791e71fc01",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "3a50ea06-b97c-460d-a79f-de06c5ca4093",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "e1680e45-c334-425f-8b62-acedfd4357ac",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "22b96e2f-03ba-4096-b787-40c07abe9bea",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a8601390-5d7c-45c1-8028-55224efb5477",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "6df1298d-9e42-4a86-8377-7ad542dbe2fd",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 13,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "ea3121bd-5e47-4891-9566-74303aeaf64b",
            "code": "3736091",
            "name": "Special ",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "e1680e45-c334-425f-8b62-acedfd4357ac",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "22b96e2f-03ba-4096-b787-40c07abe9bea",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a8601390-5d7c-45c1-8028-55224efb5477",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "6df1298d-9e42-4a86-8377-7ad542dbe2fd",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 14,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "f5265ff1-59c4-42eb-b06a-ee69bf45cff3",
            "code": "00635",
            "name": "Roller meniu rinkinys",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "3b8a8ffe-ea6e-41d4-86df-f159809585a8",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "e1680e45-c334-425f-8b62-acedfd4357ac",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "22b96e2f-03ba-4096-b787-40c07abe9bea",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a8601390-5d7c-45c1-8028-55224efb5477",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "6df1298d-9e42-4a86-8377-7ad542dbe2fd",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "06119ba2-0def-4138-bd09-d3142b0070ea",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "864653b0-dd39-4f74-9a3b-dd791e71fc01",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "3a50ea06-b97c-460d-a79f-de06c5ca4093",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 15,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "e1221908-8cf2-402e-8992-445ca79b1a41",
            "code": "00520",
            "name": "Medium Meniu",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [
                {
                    "id": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
                    "minAmount": 2,
                    "maxAmount": 2,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "7d3705b7-520e-4ef0-8c31-2753138eedbd",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a254aba5-589b-4a84-bd90-3d1d6ad02b8c",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a9060632-78f1-41ee-b41f-6a22345b5a89",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "31081e5e-2519-4261-810e-6a6564854034",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "d557d516-b279-476a-a901-ffaa871e67e5",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 16,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "4f8fde84-d612-4680-ba6f-772150e6356b",
            "code": "3736104",
            "name": "Kibirėlis 12 wings WOLTTTT",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 5.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "2ceef125-21a6-4f01-ba34-ac77cbc98f6b",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 17,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "4f88eeeb-8adb-455c-b41f-f0a7e58201e0",
            "code": "00067",
            "name": "Gira Tauras 0,5 l",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 7.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "e1680e45-c334-425f-8b62-acedfd4357ac",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "22b96e2f-03ba-4096-b787-40c07abe9bea",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a8601390-5d7c-45c1-8028-55224efb5477",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "6df1298d-9e42-4a86-8377-7ad542dbe2fd",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 18,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "90c267e2-74d1-4483-8c02-b2aebfc97b6c",
            "code": "00634",
            "name": "Felix burger rinkinys",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "56a1b8c0-326d-4d4a-b3e1-bcbc8831ad9e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 19,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "7347247b-5364-4a3c-a28f-3cd6cdb9db0b",
            "code": "00578",
            "name": "Felix burger",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 20,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "a85a7368-3801-4c2b-9b71-9d8d56f8f302",
            "code": "00537",
            "name": "Didelė bulvyčių porcija",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "3b8a8ffe-ea6e-41d4-86df-f159809585a8",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "56a1b8c0-326d-4d4a-b3e1-bcbc8831ad9e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "e1680e45-c334-425f-8b62-acedfd4357ac",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "22b96e2f-03ba-4096-b787-40c07abe9bea",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a8601390-5d7c-45c1-8028-55224efb5477",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "6df1298d-9e42-4a86-8377-7ad542dbe2fd",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "06119ba2-0def-4138-bd09-d3142b0070ea",
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "864653b0-dd39-4f74-9a3b-dd791e71fc01",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "3a50ea06-b97c-460d-a79f-de06c5ca4093",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "a74be7cf-ace9-4036-9571-71db5457bd3d",
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "c790e296-50db-4a3b-acc4-8a85c3dadbf2",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "c1a6e1b1-ec1d-44aa-b820-988ebb733dd3",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "1266420a-0171-4a88-8356-e346d0ba90a7",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "9ce2fb04-077c-4e1a-9c2e-f5683aca8d15",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 21,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "c42a2656-73b9-43ba-9831-1893b15616ae",
            "code": "00664",
            "name": "Combo Meniu",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 22,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "ff806d1a-c48d-479d-87ae-59753c13c9d4",
            "code": "00090",
            "name": "Chiquitto Rinkinys",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 23,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "95f4483d-f362-4e0a-b98a-acf5cbac74e4",
            "code": "00574",
            "name": "Cheese Felix burgeris",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 24,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "be1ec3bf-2afe-4f8e-a271-f8fc43e6ffeb",
            "code": "00565",
            "name": "Cezario salotos",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 5.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 25,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "f5885734-b073-488f-b3d9-af9246340c5d",
            "code": "00053",
            "name": "BBQ padažas",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "56a1b8c0-326d-4d4a-b3e1-bcbc8831ad9e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 99,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "92fce317-d5fe-4a45-80fd-0ec58ecae421",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "b17ca4ca-1d42-44e6-84e9-77ab505481c6",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "6bc6d75e-f0e6-4df1-80de-b4486db2b8b8",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "e1680e45-c334-425f-8b62-acedfd4357ac",
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "22b96e2f-03ba-4096-b787-40c07abe9bea",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "a8601390-5d7c-45c1-8028-55224efb5477",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "6df1298d-9e42-4a86-8377-7ad542dbe2fd",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 26,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "19c7a512-61e4-45e1-8ba7-966786a88f95",
            "code": "00003",
            "name": "BBQ jautienos mėsainio rinkinys",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 1,
                    "minAmount": 1,
                    "maxAmount": 1,
                    "required": "true",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 27,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "765b95b9-9de7-4216-a83a-7fd23860ce5a",
            "code": "00569",
            "name": "Bacon Cheese burgeris",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 28,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "dcf4d58c-4067-466e-b583-e775f67b1700",
            "code": "00584",
            "name": "00584",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 29,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "3bf52181-9e2d-4ceb-9ebd-37bf12183c96",
            "code": "00581",
            "name": "00581",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "083a2f96-5657-4204-b3f7-2fbd21a0824b",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0d",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "pcs",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "cf243fe6-6818-4ada-90c4-507a1e7a947d",
            "order": 3,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "4c88eb0f-b904-4ab6-a58f-4efe594b53d4",
            "code": "3401",
            "name": "3401",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 10.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 90.0,
            "fatFullAmount": 100.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 900.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 30,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "d42caceb-51d6-448f-a724-1ba4da1345b0",
            "code": "00047",
            "name": "00047",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "083a2f96-5657-4204-b3f7-2fbd21a0824b",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0d",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 31,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "3beeefe5-f955-4aa9-a677-5d1d5ea0a081",
            "code": "00580",
            "name": "00580",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "9611e648-7f7a-473a-899a-c3557cc10318",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "cee3cc94-b141-4359-8a72-674d586d31d8",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "10a410d9-0416-497c-959a-398fd2287d09",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "e615ac0d-3169-4f82-8e4d-6aeef32949ca",
            "code": "609331",
            "name": "Sake sashimi",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "7f08696c-c05a-4e4f-a8a7-e0eb8dc4cc96",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "cee3cc94-b141-4359-8a72-674d586d31d8",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "7a4dbc8d-00c3-487a-866d-a06db8f2a8df",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "c719d752-93b5-4ddb-b8d4-5b375f46f326",
            "code": "2901",
            "name": "15. Black tuna (8 vnt.)",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "7f08696c-c05a-4e4f-a8a7-e0eb8dc4cc96",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "cee3cc94-b141-4359-8a72-674d586d31d8",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "7a4dbc8d-00c3-487a-866d-a06db8f2a8df",
            "order": 1,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "f7d1f5ed-fe82-471b-9242-f3290f8c965e",
            "code": "605041",
            "name": "23. Easy sake maki (8 vnt.)",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "7f08696c-c05a-4e4f-a8a7-e0eb8dc4cc96",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "cee3cc94-b141-4359-8a72-674d586d31d8",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "7a4dbc8d-00c3-487a-866d-a06db8f2a8df",
            "order": 2,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "a38cb765-5327-481e-8531-5d559e7bca23",
            "code": "603051",
            "name": "24. Nato maki (8 vnt.)",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "af72b438-2a70-4e2d-b71a-04ada1f4736b",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
                    "minAmount": 0,
                    "maxAmount": 10,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 32,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "1f160407-a4a2-4bcc-8c56-1d7f0718e247",
            "code": "30110",
            "name": "VP Fajita su plėšyta kiauliena",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                },
                {
                    "id": "3badf7ad-79cd-46c8-af56-23a60f7c9118",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
                    "minAmount": 0,
                    "maxAmount": 10,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 33,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "fb7b9486-fd10-4720-b4de-f3b680b606b7",
            "code": "178.0",
            "name": "VP Burita bowl su menke panko plutelėje",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "6c926384-dc9a-4cb8-99f2-03ac8ef61272",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 34,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "3badf7ad-79cd-46c8-af56-23a60f7c9118",
            "code": "362.0",
            "name": "Gal tortilijos ar kesadilijos? (VP)",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "6c926384-dc9a-4cb8-99f2-03ac8ef61272",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 35,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "105c46c7-e9b7-4290-8b85-eabecef23294",
            "code": "784.0",
            "name": "Ant kepsninės grilinta tortilija (VP)",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [
                {
                    "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
                    "defaultAmount": 0,
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "hideIfDefaultAmount": "false",
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "groupModifiers": [
                {
                    "id": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
                    "minAmount": 0,
                    "maxAmount": 1,
                    "required": "false",
                    "childModifiersHaveMinMaxRestrictions": "false",
                    "childModifiers": [
                        {
                            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        },
                        {
                            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
                            "defaultAmount": 0,
                            "minAmount": 0,
                            "maxAmount": 0,
                            "required": "false",
                            "hideIfDefaultAmount": "false",
                            "splittable": "false",
                            "freeOfChargeAmount": 0
                        }
                    ],
                    "hideIfDefaultAmount": "false",
                    "defaultAmount": 0,
                    "splittable": "false",
                    "freeOfChargeAmount": 0
                }
            ],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 36,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "74be8f80-f2f3-4ff3-bdfb-e854b58500aa",
            "code": "2190.0",
            "name": "VP Churros su karamelės padažu",
            "description": "",
            "additionalInfo": "null",
            "tags": [],
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.500000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "c790e296-50db-4a3b-acc4-8a85c3dadbf2",
            "code": "00010",
            "name": "Mėtų",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.500000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "c1a6e1b1-ec1d-44aa-b820-988ebb733dd3",
            "code": "00013",
            "name": "Braškių",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.500000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "1266420a-0171-4a88-8356-e346d0ba90a7",
            "code": "00011",
            "name": "Bananų 2",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.500000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "a74be7cf-ace9-4036-9571-71db5457bd3d",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "9ce2fb04-077c-4e1a-9c2e-f5683aca8d15",
            "code": "00012",
            "name": "Cinamono",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "52c79bcb-04ac-42ef-b8e4-89d8719d8e40",
            "code": "11111230181",
            "name": "11111230181",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "576d5240-688b-4188-a3e1-9ff9d0c5148b",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "81138672-1987-4b7a-9614-dcb00eba1734",
            "code": "11111230180",
            "name": "11111230180",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "06119ba2-0def-4138-bd09-d3142b0070ea",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "06119ba2-0def-4138-bd09-d3142b0070ea",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "864653b0-dd39-4f74-9a3b-dd791e71fc01",
            "code": "00273",
            "name": "Rytietiškos morkų salotos",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "06119ba2-0def-4138-bd09-d3142b0070ea",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "06119ba2-0def-4138-bd09-d3142b0070ea",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "3a50ea06-b97c-460d-a79f-de06c5ca4093",
            "code": "00063",
            "name": "Coleslaw salotos",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "e1680e45-c334-425f-8b62-acedfd4357ac",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "e1680e45-c334-425f-8b62-acedfd4357ac",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "22b96e2f-03ba-4096-b787-40c07abe9bea",
            "code": "00018",
            "name": "cola",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 1.0,
            "groupId": "e1680e45-c334-425f-8b62-acedfd4357ac",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "kg",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 10.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "e1680e45-c334-425f-8b62-acedfd4357ac",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "a8601390-5d7c-45c1-8028-55224efb5477",
            "code": "132",
            "name": "Mirinda 0,33l",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "e1680e45-c334-425f-8b62-acedfd4357ac",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "e1680e45-c334-425f-8b62-acedfd4357ac",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "6df1298d-9e42-4a86-8377-7ad542dbe2fd",
            "code": "00240",
            "name": "pepsi",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "7d3705b7-520e-4ef0-8c31-2753138eedbd",
            "code": "00061",
            "name": "be padazo",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "a254aba5-589b-4a84-bd90-3d1d6ad02b8c",
            "code": "00056",
            "name": "Aštrus  p.",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "a9060632-78f1-41ee-b41f-6a22345b5a89",
            "code": "00058",
            "name": "cesnakinis",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "31081e5e-2519-4261-810e-6a6564854034",
            "code": "00054",
            "name": "keciupas",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "0eb3ba89-3a09-45d6-8465-731ec6b2100a",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "d557d516-b279-476a-a901-ffaa871e67e5",
            "code": "00057",
            "name": "Barbecue  p.",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "af72b438-2a70-4e2d-b71a-04ada1f4736b",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "af72b438-2a70-4e2d-b71a-04ada1f4736b",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "a2b41bc8-5826-4734-8a98-10ffa7a01d1f",
            "code": "015",
            "name": "015",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "56a1b8c0-326d-4d4a-b3e1-bcbc8831ad9e",
            "code": "00004",
            "name": "Wolt modif nera",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "3b8a8ffe-ea6e-41d4-86df-f159809585a8",
            "code": "00550",
            "name": "pakuote 40",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "8745e2c3-fa54-4d34-9af5-03ace6e0b99e",
            "code": "00549",
            "name": "Pakuotės mokestis",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.100000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "2ceef125-21a6-4f01-ba34-ac77cbc98f6b",
            "code": "00079",
            "name": "Depozito mokestis",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "92fce317-d5fe-4a45-80fd-0ec58ecae421",
            "code": "00039",
            "name": "Traškūs svogūnėliai",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "0f598026-aabf-4a95-0186-415a50d66f0f",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "b17ca4ca-1d42-44e6-84e9-77ab505481c6",
            "code": "00040",
            "name": "Bulvytės naminio stiliaus",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "6bc6d75e-f0e6-4df1-80de-b4486db2b8b8",
            "code": "00048",
            "name": "Mūsų gamybos majonezas",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "null",
            "productCategoryId": "null",
            "type": "Modifier",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "false",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "null",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "cee3cc94-b141-4359-8a72-674d586d31d8",
            "code": "608141",
            "name": "Pridėti medinius pagaliukus",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        },
        {
            "fatAmount": 0.0,
            "proteinsAmount": 0.0,
            "carbohydratesAmount": 0.0,
            "energyAmount": 0.0,
            "fatFullAmount": 0.0,
            "proteinsFullAmount": 0.0,
            "carbohydratesFullAmount": 0.0,
            "energyFullAmount": 0.0,
            "weight": 0.0,
            "groupId": "6c926384-dc9a-4cb8-99f2-03ac8ef61272",
            "productCategoryId": "null",
            "type": "Dish",
            "orderItemType": "Product",
            "modifierSchemaId": "null",
            "modifierSchemaName": "null",
            "splittable": "false",
            "measureUnit": "serv",
            "sizePrices": [
                {
                    "sizeId": "null",
                    "price": {
                        "currentPrice": 0.000000000,
                        "isIncludedInMenu": "true",
                        "nextPrice": "null",
                        "nextIncludedInMenu": "false",
                        "nextDatePrice": "null"
                    }
                }
            ],
            "modifiers": [],
            "groupModifiers": [],
            "imageLinks": [],
            "doNotPrintInCheque": "false",
            "parentGroup": "6c926384-dc9a-4cb8-99f2-03ac8ef61272",
            "order": 0,
            "fullNameEnglish": "",
            "useBalanceForSell": "false",
            "canSetOpenPrice": "false",
            "id": "3badf7ad-79cd-46c8-af56-23a60f7c9118",
            "code": "362.0",
            "name": "Gal tortilijos ar kesadilijos? (VP)",
            "description": "",
            "additionalInfo": "null",
            "tags": "null",
            "isDeleted": "false",
            "seoDescription": "null",
            "seoText": "null",
            "seoKeywords": "null",
            "seoTitle": "null"
        }
    ],
    "sizes": [],
    "revision": 1677225362977
}
        self.iiko_patiekalai = self.iiko_meniu["products"]
        

    def bolt_iiko_lyginimas(self):
        patiekalo_info = list(filter(lambda x: x['code'] == self.sku, self.iiko_patiekalai))
        print(patiekalo_info)

        # z = json.dumps(patiekalo_info)
        # v = json.loads(z)
        patiekalo_iiko_id = patiekalo_info[0]["id"]
        print(patiekalo_iiko_id)
        





for patiekalas in bolt_patiekalu_informacija:
    bolt_patiekalas = Bolt_patiekalu_info(patiekalas)
    bolt_patiekalas = bolt_patiekalas.bolt_iiko_lyginimas()