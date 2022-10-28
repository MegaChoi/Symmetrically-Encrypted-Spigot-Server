package legacyStuffs;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.Mac;
import java.util.Base64;
public class sha {
    public static void main(String [] aStrings) throws Exception{
        SecretKeySpec keySpec = new SecretKeySpec(
        "McQfThWmZq4t7w!z%C*F-JaNdRgUkXnz".getBytes("UTF-8"),
        "HmacSHA256");
        
        // byte[] utf8 = "xAZucg2kSrwuOtsgXr4RWA==".getBytes("UTF-8");
        // byte[] base64 = Base64.getUrlDecoder().decode(utf8);
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(keySpec);
        byte[] result = mac.doFinal("nice".getBytes());

        System.out.println(Base64.getEncoder().encodeToString(result));
    }
}
