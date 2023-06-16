public class Conversion {

    public String solution(int n) {
        int[] values = { 1000, 900, 800, 500, 400, 100, 90, 80, 50, 40, 10, 9, 8, 5, 4, 1 };
        String[] symbols = { "M", "CM", "DCCC", "D", "CD", "C", "XC", "LXXX", "L", "XL", "X", "IX", "VIII", "V", "IV", "I" };
        
      
        StringBuilder resultado = new StringBuilder();
        
        for (int i = 0; i<values.length; i++){
          int value = values[i];
          while(n >= value){
            n -= value;
            resultado.append(symbols[i]);
          }
        }
        return resultado.toString();
      }
}
