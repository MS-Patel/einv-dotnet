import base64
import json
import clr
# ___________________________________________Dot Net Code_____________________________________________
from System.Reflection import Assembly
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\System.Net.Http.Extensions.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\System.Net.Http.Primitives.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\System.Net.Http.Formatting.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\BouncyCastle.Crypto.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\Newtonsoft.Json.dll")

clr.AddReference("dll/Calc")
clr.AddReference("System.Net.Http.Extensions")
clr.AddReference("System.Net.Http.Primitives")
clr.AddReference("System.Net.Http.Formatting")
clr.AddReference("Newtonsoft.Json")
# ___________________________________________Python Code_____________________________________________
from Calc import Program

# conn = pyodbc.connect(
#     "Driver={ODBC Driver 17 for SQL Server};" "Server=DESKTOP-FV0B6MO\SQLEXPRESS;" "uid=msp;" "pwd=msp@123;" "Database=invoice;" "Trusted_Connection=no;")


# def read(conn):
#     cursor = conn.cursor()
#     cursor.execute(
#         "select * from invoice_details where EInvoice_Status = 'false'")

    # for inv in cursor:
    #     jsondata = {"Version": "1.1",
    #                 "TranDtls": {
    #                     "TaxSch": "GST",
    #                     "SupTyp": "B2B",
    #                     "RegRev": "N",
    #                     "EcmGstin": 'null',
    #                     "IgstOnIntra": 'N'  # if inv.Buyer_StateCode = 24 ? 'N':'Y',
    #                 },
    #                 "DocDtls": {
    #                     "Typ": "INV",  # if condition CategoryName,
    #                     "No": inv.DocumentNo,
    #                     "Dt": inv.DocumentDate
    #                 },
    #                 "SellerDtls": {
    #                     "Gstin": inv.Company_GSTNo,
    #                     "LglNm": inv.LegalName,
    #                     "TrdNm": inv.TradeName,
    #                     "Addr1": inv.Address1,
    #                     "Addr2": inv.Address2,
    #                     "Loc": inv.City,
    #                     "Pin": inv.PinCode,
    #                     "Stcd": inv.StateCode,
    #                     "Ph": inv.Phone,
    #                     "Em": inv.EMail
    #                 },
    #                 "BuyerDtls": {
    #                     "Gstin": inv.Buyer_GSTIN,
    #                     "LglNm": inv.Buyer_LegalName,
    #                     "TrdNm": inv.Buyer_TradeName,
    #                     "Pos": inv.Consg_StateCode,  # if exportinvoice : 96
    #                     "Addr1": inv.Buyer_Address1,
    #                     "Addr2": inv.Buyer_Address2,
    #                     "Loc": inv.Buyer_CityName,
    #                     "Pin": inv.Buyer_PinCode,
    #                     "Stcd": inv.Buyer_StateCode,
    #                     "Ph": inv.Buyer_Phone,
    #                     "Em": inv.Buyer_Email
    #                 },
    #                 "DispDtls": {
    #                     "Nm": inv.LegalName,
    #                     "Addr1": inv.Address1,
    #                     "Addr2": inv.Address2,
    #                     "Loc": inv.City,
    #                     "Pin": inv.PinCode,
    #                     "Stcd": inv.StateCode
    #                 },
    #                 "ShipDtls": {
    #                     "Gstin": inv.Consg_GSTIN,
    #                     "LglNm": inv.Consg_LegalName,
    #                     "TrdNm": inv.Consg_TradeName,
    #                     "Addr1": inv.Consg_Address1,
    #                     "Addr2": inv.Consg_Address2,
    #                     "Loc": inv.Consg_CityName,
    #                     "Pin": inv.Consg_PinCode,
    #                     "Stcd": inv.Consg_StateCode
    #                 },
    #                 "ItemList": [{
    #                     "SlNo": inv.SerialNo,
    #                     "PrdDesc": inv.Product_Description,
    #                     "IsServc": 'N',  # if inv.CategoryName = 'Service Invoice' ? 'Y':'N',,
    #                     "HsnCd": inv.HSNCode,
    #                     "Barcde": inv.Barcode,
    #                     "Qty": inv.Quantity,
    #                     "FreeQty": inv.FreeQty,
    #                     "Unit": 'NUMBERS',  # if inv.Unit = 'NOS' ? 'NUMBERS' : 'OTHERS',
    #                     "UnitPrice": inv.Rate,
    #                     "TotAmt": inv.ItemAmount,
    #                     "Discount": inv.DiscountAmount,
    #                     "PreTaxVal": inv.Ass_Value,
    #                     "AssAmt": inv.Ass_Value,
    #                     "GstRt": 18,  # if IGST ? IGST : CGST+SGST,
    #                     "SgstAmt": inv.ITM_SGST,
    #                     "IgstAmt": inv.ITM_IGST,
    #                     "CgstAmt": inv.ITM_CGST,
    #                     "CesRt": 0,
    #                     "CesAmt": 0,
    #                     "CesNonAdvlAmt": 0,
    #                     "StateCesRt": 0,
    #                     "StateCesAmt": 0,
    #                     "StateCesNonAdvlAmt": 0,
    #                     "OthChrg": 0,
    #                     "TotItemVal": inv.ItemAmount + inv.ITM_SGST + inv.ITM_CGST + inv.ITM_IGST,
    #                 }],
    #                 "ValDtls": {
    #                     "AssVal": inv.AssValue,
    #                     "CgstVal": inv.INV_CGST,
    #                     "SgstVal": inv.INV_SGST,
    #                     "IgstVal": inv.INV_IGST,
    #                     "CesVal": inv.Cess,
    #                     "StCesVal": inv.StateCess,
    #                     "Discount": inv.Discount,
    #                     "OthChrg": inv.OtherCharges,
    #                     "RndOffAmt": inv.RoundOff,
    #                     "TotInvVal": inv.Total_InvValue,
    #                     "TotInvValFc": inv.Total_ValueAfterDisc
    #                 },
    #                 # "ExpDtls": {
    #                 #     "ShipBNo": inv.ShipBNo,
    #                 #     "ShipBDt": inv.ShipBDt,
    #                 #     "Port": inv.Port,
    #                 #     "RefClm": inv.RefClm,
    #                 #     "ForCur": inv.ForCur,
    #                 #     "CntCode": inv.CntCode,
    #                 #     "ExpDuty": inv.ExpDuty
    #                 # },
    #                 "EwbDtls": {
    #                     "TransId": inv.TR_GSTIN,
    #                     "TransName": inv.TransporterName,
    #                     "Distance": inv.Distance,
    #                     "TransDocNo": inv.TR_DOc_No,
    #                     "TransDocDt": inv.TR_Doc_Date,
    #                     "VehNo": inv.VehicleNo,
    #                     "VehType": inv.VehicleType,
    #                     "TransMode": inv.TR_Mode
    #                 }
    #                 }
    #     return jsondata


# jsondata = (read(conn))
jsondata = {
    "Version": "1.1",
    "UserGstin": "29ABLPK6554F000",
    "TranDtls": {
        "SupTyp": "B2B",
        "RegRev": "N",
        "TaxSch": "GST",
        "IgstOnIntra": "N"
    },
    "DocDtls": {
        "Typ": "INV",
        "No": "MAR119",
        "Dt": "11/05/2022"
    },
    "SellerDtls": {
        "LglNm": "Borkar Packaging Pvt. Ltd.",
        "Gstin": "29ABLPK6554F000",
        "Addr1": "Address1",
        "Loc": "Hydrabad",
        "Stcd": "29",
        "Pin": 560001
    },
    "BuyerDtls": {
        "LglNm": "Shalibhadra Finance Limited",
        "Gstin": "37ABLPK6554F002",
        "Pos": "37",
        "Addr1": "Address1",
        "Loc": "Hydrabad",
        "Stcd": "37",
        "Pin": 518001
    },
    "ValDtls": {
        "AssVal": 2000,
        "IgstVal": 360,
        "CgstVal": 0,
        "SgstVal": 0,
        "CesVal": 0,
        "StCesVal": 0,
        "TotInvVal": 2360
    },
    "itemList": [{
        "SlNo": "1",
        "PrdDesc": "Abc",
        "IsServc": "N",
        "HsnCd": "390110",
        "Qty": 10,
        "Unit": "SQM",
        "UnitPrice": 100,
        "TotAmt": 1000,
        "Discount": 0,
        "AssAmt": 1000,
        "GstRt": 18,
        "IgstAmt": 180,
        "TotItemVal": 1180
    }, {
        "SlNo": "2",
        "PrdDesc": "Abc",
        "IsServc": "N",
        "HsnCd": "100110",
        "Qty": 100,
        "Unit": "SQM",
        "UnitPrice": 10,
        "TotAmt": 1000,
        "Discount": 0,
        "AssAmt": 1000,
        "GstRt": 18,
        "IgstAmt": 180,
        "TotItemVal": 1180
    }]
}
# ___________________________________________Dot Net Code_____________________________________________

obj = Program()

sek = obj.call_server_api()
print(sek)
jsondata = base64.urlsafe_b64encode(json.dumps(jsondata).encode()).decode()
# jsondata = base64.b64encode(jsondata.encode())
# jsondata = base64.b64decode(jsondata)
# sek = base64.b64encode(sek.encode())
# sek = base64.b64decode(sek)

res = obj.EncryptBySymmetricKey(jsondata, sek, "PSyL7I1NXqaRf5bq5FU0d63e7")
try:
    result = json.loads(res)
    print(result)
except:
    result = json.loads(base64.urlsafe_b64decode(res.encode()).decode())
    print(result)

