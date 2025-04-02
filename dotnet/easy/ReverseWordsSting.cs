using System.Collections;
using System.Net.Mail;
using System.Text;

public class ReverseWordsSting
{
    public string ReverseWords(string s)
    {
        StringBuilder sb = new StringBuilder(s);
        int lastSpace = 0;

        for (int left = 0, right = 0; right < sb.Length; right++)
        {

            if (sb[right].Equals(' ') || left < lastSpace || right == sb.Length - 1)
            {
                lastSpace = right;

                if (right < sb.Length - 1)
                    right--;
                    
                while (left < right)
                {
                    char rightChar = sb[right];
                    sb[right] = s[left];
                    sb[left] = rightChar;
                    left++;
                    right--;
                }

                right = lastSpace + 1;
                left = lastSpace + 1;
            }
        }

        return sb.ToString();
    }
}