using System.Text;

public class RemovableCharactersString
{
    public List<int> RemovableCharacters(string str1, string str2)
    {
        char targetChar;
        List<int> ind = new List<int>();
        StringBuilder sb1 = new StringBuilder(str1);
        StringBuilder sb2 = new StringBuilder(str2);

        for (int i = 0; i <= sb1.Length - 1; i++)
        {
            if (i < sb2.Length)
            {
                if (!sb1[i].Equals(sb2[i]))
                {
                    ind.Add(i);

                    targetChar = sb1[i];

                    if (sb1[i + 1].Equals(sb2[i]))
                    {
                        for (int x = i; x >= 0; x--)
                        {
                            if (sb1[x].Equals(sb2[x]) && sb1[x] == targetChar)
                            {
                                ind.Add(x);
                            }
                        }

                        return ind;
                    }
                }
            }
        }
        
        return ind;
    }
}