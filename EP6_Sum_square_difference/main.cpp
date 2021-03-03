//EP6 Sum square difference
/*
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
*/


#include <QCoreApplication>
#include <QDebug>


int sum(int n)
//Returns the sum of the first n integers
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
        sum+=i;
    return sum;
}

int square(int n)
//Returns the square of n
{
    return n*n;
}

int sumOfSquares(int n)
//Returns the sum of squares for the first n integers
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum+=square(i);
    }
    return sum;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    int k = 100;
    int s = sum(k);
    int sq = square(s);
    int ss = sumOfSquares(k);
    qDebug() << "sum " << k << ": " << s;
    qDebug() << "Square of " << s << ": " << sq;
    qDebug() << "Sum of squares of " << k << ": " << sumOfSquares(k);
    qDebug() << "Difference of sum of squares and squares of sum: " << sq-ss;

    return a.exec();
}
