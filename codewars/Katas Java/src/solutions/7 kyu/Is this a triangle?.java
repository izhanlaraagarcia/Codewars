import static org.junit.Assert.*;
import org.junit.Test;

class TriangleTester{
  public static boolean isTriangle(int a, int b, int c){
//     || = or
    if (a <= 0 || b <= 0 || c <= 0){
      return false;
    } else{
//       && = and
      return (a + b) > c && (a + c) > b && (b + c) > a;
    }
  }
}
