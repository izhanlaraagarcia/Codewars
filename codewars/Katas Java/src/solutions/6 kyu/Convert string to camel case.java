import java.lang.StringBuilder;
class Solution{

  static String toCamelCase(String s){
        String[] words = s.split("[-_]");
        StringBuilder result = new StringBuilder(words[0]);

        for (int i = 1; i < words.length; i++) {
            String word = words[i];
            result.append(Character.toUpperCase(word.charAt(0))).append(word.substring(1));
        }

        return result.toString();
    }
}
