using System.Collections;
using System.Net.Mail;
using System.Text;

public class ReverseWordsSting {
    public string ReverseWords(string s) {
        StringBuilder sb = new StringBuilder(s);

        for (int left = 0, right = 0; right < sb.Length; right++) {

            if(sb[right].Equals(' ')){
                char rightChar = sb[right-1];
                sb[right-1] = s[left];
                sb[left] = rightChar;
            }
        }

        return sb.ToString();
    }
}