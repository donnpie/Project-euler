//EP7 10001st prime
//By listing the first six prime numbers:
//2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//What is the 10 001st prime number?

#include <QCoreApplication>
#include <QDebug>
#include <QList>

void init(QList<int> &l)
//Sets up the first few primes
{
    l.push_back(1);
    l.push_back(2);
    l.push_back(3);
    l.push_back(5);
    l.push_back(7);
    l.push_back(11);
}


int prime(int n, QList<int> &l)
//Return the nth prime number
//l is a list of prime numbers
{
    int i; //index
    int j; //prime number
    int k; //divisor for determining prime number
    int w = 0; //watchdog
    int s = l.size();
    bool isNotPrime = true;
    if (n < s)
    {
        qDebug() << "n < s, returning l[n] = " << l[n];
        return l[n];
    }
    else {
        j = l[s-1]+2;
        for (i = s; i <= n; i++)
        {
            isNotPrime = true;
            w = 0;
            while (isNotPrime)
            {
                //qDebug() << "Searching i = " << i;
                for (k = 3; k < j/2; k+=2) //k is the divisor
                {
                    //qDebug() << "\tSearching i = " << i << ", k = " << k << ", j = " << j;
                    if (j%k == 0) //Test if j is a prime
                    {
                        isNotPrime = true;
                        //qDebug() << "\t\t" << j << " is not a prime";
                        break;
                    }
                    else {
                        isNotPrime = false;
                    }
                }
                if (!isNotPrime) //j is a prime number
                {
                    l.push_back(j);
                    //qDebug() << "\t\tFound l[i]: l[" << i << "] = " << l[i] << " at k = " << k;
                    isNotPrime = false;
                }
                w++;
                if (w > 100)
                    break;
                j+=2; //Move to the next number
            }
        }
        return l[n];
    }
}


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QList<int> l;
    init(l);
    int ans = 0;
    int index = 10001;
    ans = prime(index, l);
    qDebug() << "The " << index << "th prime is " << ans;

    return a.exec();
}
