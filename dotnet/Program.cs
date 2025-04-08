
public class Program
{
    public static void Main(string[] args)
    {

        //Reverse Words in a String III (Leetcode)
        string input = "Let's take LeetCode contest";
        ReverseWordsString reverseWordsSting = new ReverseWordsString();
        Console.WriteLine("Reverse Words in a String III (Leetcode)");
        Console.WriteLine("             Input: " + input);
        Console.WriteLine("             Output: " + reverseWordsSting.ReverseWords(input));

        //Removable Characters in a String (HackerRank Interview)
        string str1 = "abdgggda";
        string str2 = "abdggda";
        RemovableCharactersString removableCharactersString = new RemovableCharactersString();
        Console.WriteLine("Removable Characters in a String (HackerRank Interview)");
        foreach (int item in removableCharactersString.RemovableCharacters(str1, str2))
            Console.WriteLine("            Output Index: " + item);



    }
}