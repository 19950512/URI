using System;
class ClassMain {
    static void Main() {
        float raio = float.Parse(Console.ReadLine());
        float pi = 3.14159;

        float area = (raio * raio) * pi;

        string resposta = String.Concat("A=%.4f\n", area);

        Console.WriteLine(resposta);
    }
}