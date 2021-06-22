using System;
class ClassMain {
    static void Main() {
        int a = Convert.ToInt32(Console.ReadLine());
        int b = Convert.ToInt32(Console.ReadLine());
        int x = a + b;

        string resposta = String.Concat("X = ", x);

        Console.WriteLine(resposta);
    }
}