using System.Text;

public class RemovableCharactersString
{

    public List<int> RemovableCharacters(string str1, string str2) 
    {
        List<int> ind = new List<int>();
        StringBuilder sb1 = new StringBuilder(str1);
        StringBuilder sb2 = new StringBuilder(str2);

        for (int i=0; i <= sb2.Length-1; i++)
        {
            if(!sb1[i].Equals(sb2[i])) 
            {
                ind.Add(i);
            }
        }

        return ind;

    }


}