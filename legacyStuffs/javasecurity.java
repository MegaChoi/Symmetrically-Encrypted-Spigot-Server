package legacyStuffs;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import javax.crypto.Mac;
public  class  javasecurity { 
    public static void main(String[] arg){
        String key = "twentyfourcharacters1111";
        String MACkey = "McQfThWmZq4t7w!z%C*F-JaNdRgUkXnz";
        String original_MAC = "xGjRnnE45tS2ZPyWTorlOg9Ldu/6fwMvCdkQTO42j4o=";
        String initVector = "jvHJ1XFt0IXBrxxx";
        String ciphertext = "xAZucg2kSrwuOtsgXr4RWA==";

        try {
            // testing keys
            IvParameterSpec iv = new IvParameterSpec(initVector.getBytes("UTF-8"));
            SecretKeySpec key1 = new SecretKeySpec(key.getBytes("UTF-8"), "AES");
            SecretKeySpec key2 = new SecretKeySpec(MACkey.getBytes("UTF-8"), "HmacSHA256");

            // MAC module
            byte[] utf8 = "xAZucg2kSrwuOtsgXr4RWA==".getBytes("UTF-8");
            byte[] base64 = Base64.getUrlDecoder().decode(utf8);
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(key2);
            byte[] result = mac.doFinal(base64);

            // if this mac value == original mac value from python then decrypt
            if (Base64.getEncoder().encodeToString(result).equals(original_MAC)){
                // decryption module
                Cipher cipherd = Cipher.getInstance("AES/CBC/PKCS5PADDING");
                cipherd.init(Cipher.DECRYPT_MODE, key1, iv);
                byte[] original = cipherd.doFinal(Base64.getDecoder().decode(ciphertext));
                String decryptedResult = new String(original);
                System.out.println("Decrypted string: " + decryptedResult);
            }

            
            
            return;
        } catch (Exception ex) {
            ex.printStackTrace();
        }
     }
}