using Newtonsoft.Json;
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Security;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

using System.Diagnostics;
using IronPython.Hosting;

namespace app
{
    class Program
    {
        static void Main(string[] args)
        {
            var engine = Python.CreateEngine();
            String FileName = "script.py";
            var source = engine.CreateScriptSourceFromFile(FileName);

            var argv= new List<string>();
            argv.Add("");

            engine.GetSysModule().SetVariable("argv",argv);
            var eIO = engine.Runtime.IO;

            var results = new MemoryStream();
            eIO.SetOutput(results, Encoding.Default);
            try{
            var scope = engine.CreateScope();
            source.Execute(scope);
            }
            catch (Exception){
                Console.WriteLine("error");
            }
            Console.WriteLine(results);
            // call_server_api();
        }
        public static void call_server_api()
        {
            try
            {
                
                string public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArxd93uLDs8HTPqcSPpxZ\nrf0Dc29r3iPp0a8filjAyeX4RAH6lWm9qFt26CcE8ESYtmo1sVtswvs7VH4Bjg/F\nDlRpd+MnAlXuxChij8/vjyAwE71ucMrmZhxM8rOSfPML8fniZ8trr3I4R2o4xWh6\nno/xTUtZ02/yUEXbphw3DEuefzHEQnEF+quGji9pvGnPO6Krmnri9H4WPY0ysPQQ\nQd82bUZCk9XdhSZcW/am8wBulYokITRMVHlbRXqu1pOFmQMO5oSpyZU3pXbsx+Ox\nIOc4EDX0WMa9aH4+snt18WAXVGwF2B4fmBk7AtmkFzrTmbpmyVqA3KO2IjzMZPw0\nhQIDAQAB\n";
                HttpClient client = new HttpClient();
                string uri = "https://sandbox.shipandsmile.com/e_invoice_enc/eivital/v1.04/auth";
                client.DefaultRequestHeaders.Add("client_id", "sandboxRiBnPXUvT");
                client.DefaultRequestHeaders.Add("client_secret", "e4WbqLw1On2Dloa7");
                client.DefaultRequestHeaders.Add("Authorization", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjM0MTdmNDE1YjViMDM5MDRhOWJiZDkiLCJpYXQiOjE2NDc2ODA1MTksImV4cCI6MjQzNjA4MDUxOX0.ehi6WFAvqZ-CaLA8itmiX_3xUWSrUKTFvFAsjJ9N6-4");
                client.DefaultRequestHeaders.Add("gstin", "29ABLPK6554F000");
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                string userName = "Shali_ei";
                string password = "Ctpl@998";
                byte[] _aeskey = generateSecureKey();
                string straesKey = Convert.ToBase64String(_aeskey);
                RequestPayloadN aRequestPayload = new RequestPayloadN();
                Auth data = new Auth();
                data.Password = password;
                data.AppKey = straesKey;
                data.UserName = userName;
                data.ForceRefreshAccessToken = false;
                string authStr = JsonConvert.SerializeObject(data);
                // Console.WriteLine(authStr);
                byte[] authBytes = System.Text.Encoding.UTF8.GetBytes(authStr);
                aRequestPayload.Data = Encrypt(Convert.ToBase64String(authBytes), public_key);

                // Console.WriteLine(aRequestPayload.Data);
                string abc = JsonConvert.SerializeObject(aRequestPayload);
                // Console.WriteLine(abc);
                HttpResponseMessage res = client.PostAsJsonAsync(uri, aRequestPayload).Result;
                // Console.WriteLine(res);
                if (res.IsSuccessStatusCode)
                {
                    Console.WriteLine("Call is success");
                    string verification = res.Content.ReadAsStringAsync().Result;
                    Console.WriteLine($"Response{verification}");
                    AuthResponse authResponse = res.Content.ReadAsAsync<AuthResponse>().Result;
                    string sek = DecryptBySymmerticKey(authResponse.Data.Sek, _aeskey);
                    Console.WriteLine($"Sek {sek}");
                }
                else
                {
                    var stream = res.Content.ReadAsStreamAsync().Result;
                    StreamReader reader = new StreamReader(stream);
                    string text = reader.ReadToEnd();
                    string err = res.ReasonPhrase;
                    Console.WriteLine($"error Response{text} reason{err}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
        }
        public static string DecryptBySymmerticKey(string encryptedText, byte[] key)
        {
            try
            {
                byte[] dataToDecrypt = Convert.FromBase64String(encryptedText);
                var keyBytes = key;
                AesManaged tdes = new AesManaged();
                tdes.KeySize = 256;
                tdes.BlockSize = 128;
                tdes.Key = keyBytes;
                tdes.Mode = CipherMode.ECB;
                tdes.Padding = PaddingMode.PKCS7;
                ICryptoTransform decrypt__1 = tdes.CreateDecryptor();
                byte[] deCipher = decrypt__1.TransformFinalBlock(dataToDecrypt, 0, dataToDecrypt.Length);
                tdes.Clear();
                string EK_result = Convert.ToBase64String(deCipher);
                // var EK = Convert.FromBase64String(EK_result);
                // return EK;
                return EK_result;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }
        public static byte[] generateSecureKey()
        {
            Aes KEYGEN = Aes.Create();
            byte[] secretKey = KEYGEN.Key;
            return secretKey;
        }
        public static string Encrypt(string data, string key)
        {
            byte[] keyBytes =
            Convert.FromBase64String(key); // your key here
            AsymmetricKeyParameter asymmetricKeyParameter = PublicKeyFactory.CreateKey(keyBytes);
            RsaKeyParameters rsaKeyParameters = (RsaKeyParameters)asymmetricKeyParameter;
            RSAParameters rsaParameters = new RSAParameters();
            rsaParameters.Modulus = rsaKeyParameters.Modulus.ToByteArrayUnsigned();
            rsaParameters.Exponent = rsaKeyParameters.Exponent.ToByteArrayUnsigned();
            RSACryptoServiceProvider rsa = new RSACryptoServiceProvider();
            rsa.ImportParameters(rsaParameters);
            byte[] plaintext = Encoding.UTF8.GetBytes(data);
            byte[] ciphertext = rsa.Encrypt(plaintext, false);
            string cipherresult = Convert.ToBase64String(ciphertext);
            //string cipherresult = Encoding.ASCII.GetString(ciphertext);
            return cipherresult;
        }
       
        public static string EncryptBySymmetricKey(string jsondata, string sek)
              {
              //Encrypting SEK
              try
                 {
                    byte[] dataToEncrypt = Convert.FromBase64String(jsondata);
                    var keyBytes = Convert.FromBase64String(sek);
                    AesManaged tdes = new AesManaged();
                    tdes.KeySize = 256;
                    tdes.BlockSize = 128;
                    tdes.Key = keyBytes;
                    tdes.Mode = CipherMode.ECB;
                    tdes.Padding = PaddingMode.PKCS7;
                    ICryptoTransform encrypt__1 = tdes.CreateEncryptor();
                    byte[] deCipher = encrypt__1.TransformFinalBlock(dataToEncrypt, 0, dataToEncrypt.Length);
                    tdes.Clear();
                    string EK_result = Convert.ToBase64String(deCipher);
                    return EK_result;
                }
                    catch (Exception ex)
                       {
                         throw ex;
                       }
             }  
        public static string Decode(string token)
    {
       var parts = token.Split('.');
       var header = parts[0];
       var payload = parts[1];
       var signature = parts[2];
       byte[] crypto = Base64UrlDecode(parts[2]);
       var headerJson = Encoding.UTF8.GetString(Base64UrlDecode(header));
       var headerData = JObject.Parse(headerJson);
       var payloadJson = Encoding.UTF8.GetString(Base64UrlDecode(payload));
       var payloadData = JObject.Parse(payloadJson);        
       return headerData.ToString() + payloadData.ToString();
     }
    }
    public class Auth
    {
        public string Password { get; set; }
        public string AppKey { get; set; }
        public string UserName { get; set; }
        public Boolean ForceRefreshAccessToken { get; set; }
    }
    public class RequestPayloadN
    {
        public string Data { get; set; }
    }
    public class AuthResponse
    {
        public string Status { get; set; }
        public List<ErrorDetail> ErrorDetails { get; set; }
        public List<InfoDtl> InfoDtls { get; set; }
        public class ErrorDetail
        {
            public string ErrorCode { get; set; }
            public string ErrorMessage { get; set; }
        }
        public class InfoDtl
        {
            public string InfCd { get; set; }
            public List<Infodata> Desc { get; set; }
        }
        public class Infodata
        {
            public string ErrorCode { get; set; }
            public string ErrorMessage { get; set; }
        }
        public data Data { get; set; }
        public class data
        {
            public string ClientId { get; set; }
            public string UserName { get; set; }
            public string AuthToken { get; set; }
            public string Sek { get; set; }
            public string TokenExpiry { get; set; }
            public static implicit operator data(string v)
            {
                throw new NotImplementedException();
            }
        }
    }
}        


