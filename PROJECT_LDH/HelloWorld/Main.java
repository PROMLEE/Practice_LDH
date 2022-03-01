import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    // StringTokenizer st = new StringTokenizer(bf.readLine());
    int x, n = 0;
    int[] counts = new int[42];
    for (int i = 0; i < 10; i++) {
      x = Integer.parseInt(bf.readLine());
      x %= 42;
      if (counts[x] == 0) {
        counts[x] = 1;
        n++;
      }
    }
    sb.append(n);
    System.out.println(sb);
    bf.close();
  }
}
