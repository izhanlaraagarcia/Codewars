public class CodeWars {
  public static byte strCount(String str, char letter) {
    byte count=0;
    for (byte i = 0; i < str.length(); i++) {
    if (str.charAt(i) == letter) {
        count++;
      }
    }
    return count;
  }
}
