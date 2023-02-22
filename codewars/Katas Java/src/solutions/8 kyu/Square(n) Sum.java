public class Kata
 {
  public static int squareSum(int[] n)  { 
    int i = 0;
    int sum = 0 ;
      for (i = 0; i < n.length; i++)
        sum += n[i]*n[i];
    
    return sum;
  }
 }
