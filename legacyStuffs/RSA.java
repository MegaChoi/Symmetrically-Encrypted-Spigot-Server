package legacyStuffs;
import java.security.Key;
import java.util.Base64;
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.Security;
import java.security.interfaces.RSAPrivateCrtKey;
import java.security.interfaces.RSAPrivateKey;

import javax.crypto.spec.SecretKeySpec;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.io.File;
import java.nio.file.Files;
import java.io.FileWriter;
import java.io.IOException;
public class RSA {
    public static void main(String[] arg) throws Exception{
        String ciphertext = "Upd6uSzIY9Q1H5wjF3i9AhtrScbzJEzii0NQtAHRcmHBlO638w9JrmpDauCF0mZnDpBPT3LVv3E+w+2njXfZBumW7ohIe5NIwRa1MydMCaDTF2V2qQe14rGpxy19p/sZN8Wqff1dmMKU2WoON0rE7wDwk8ulDam3eEslmNp9bvE=";
        
        // String NEW_LINE_CHARACTER = "\n";
        String PUBLIC_KEY_START_KEY_STRING = "-----BEGIN PRIVATE KEY-----";
        String PUBLIC_KEY_END_KEY_STRING = "-----END PRIVATE KEY-----";
        String EMPTY_STRING = "";
        String private_key_String = null;

        try {
            File keyFile = new File("C:\\Users\\Duc\\OneDrive\\Desktop\\mcSecurity\\cosc2804-sep-22-assignment-3-team-48-cosc2804-sep22\\private.pem");
            byte[] privateKey = Files.readAllBytes(keyFile.toPath());
            String keyString = new String(privateKey);
            private_key_String = keyString.replace(PUBLIC_KEY_START_KEY_STRING, EMPTY_STRING).replace(PUBLIC_KEY_END_KEY_STRING, EMPTY_STRING).replaceAll(System.lineSeparator(), "");
        } catch (Exception e) {
            // TODO: handle exception
        }
        byte[] encoded = Base64.getDecoder().decode(private_key_String);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(encoded);
        PrivateKey keypriv = keyFactory.generatePrivate(keySpec);



        Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding");
        cipher.init(Cipher.DECRYPT_MODE, keypriv);
        byte[] test = cipher.doFinal(Base64.getDecoder().decode(ciphertext));
        String message = new String(test);
        System.out.print(message);
        
        // try {
        //     FileWriter myWriter = new FileWriter("C:\\Users\\ducvu\\github-classroom\\rmit-computing-technologies\\cosc2804-sep-22-assignment-3-team-48-cosc2804-sep22\\AESkey.pem");
        //     myWriter.write(message);
        //     myWriter.close();
        //     System.out.println("Successfully wrote to the file.");
        // } catch (IOException e) {
        //     System.out.println("An error occurred.");
        //     e.printStackTrace();
        //     }
    }
}   