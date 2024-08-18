import java.util.Scanner;

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        } else {
            int y = x;
            int rev = 0, r = 0;
            while (y > 0) {
                r = y % 10;
                rev = rev * 10 + r;
                y = y / 10;
            }
            return x == rev;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        Solution solution = new Solution();
        boolean result = solution.isPalindrome(number);

        System.out.println(result);

        scanner.close(); // Close the scanner to avoid resource leaks
    }
}
