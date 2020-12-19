#include <iostream>
#include <vector>

using namespace std;

struct NeighbourDot;

class Dot
{
    public:
        int h = 0; // поле, хранящее значение h()
        int g = 0; // хранит g()
        Dot *mother = nullptr; // указатель на родителя
        vector<NeighbourDot> neighbours = {}; // контейнер для указателей на соседей

        const int f() const // метод возвращающий f()
        {
            return this->g + this->h;
        }
};

struct NeighbourDot
{
    Dot* ptrToNeighb = nullptr; // указатель на соседа
    int lenBeetwen = 0; // расстояние между ними
};

// проверка на наличие элемента в векторе. Возвращает true, если aim находится в list.
bool isInList(vector<Dot*> *list, Dot *aim)
{
    for (auto i: *list)
        if (i == aim)
            return true;
    return false;
}

vector<Dot*> aStar(Dot *start, Dot *end)
{
    vector<Dot*> road;       // вектор, в который запишется искомый путь
    vector<Dot*> openedList; // открытый список
    vector<Dot*> closedList; // закрытый список
    Dot *cur = start; // указатель на вершину, которая в данный момент является текущей.
    closedList.push_back(cur);

    /* все время работы алгоритма условие будет выполняться,
    пока cur не совпадет с целевой вершиной. Тогда вектор road сразу заполнится */
    while (road.empty())
    {
        // добавление соседей текущей вершины в открытый список
        for (int i = 0; i < cur->neighbours.size(); ++i)
        {
            NeighbourDot curNeighb = cur->neighbours[i];

            /* Проверка соседей, уже находящихся в открытом списке. Если вершины не было в списке,
            то попадаем в else (записываем родителя и добавляем в открытый список).
            Если была в списке, то попадаем в if (в нем сравниваем пути) */
            if (isInList(&openedList, curNeighb.ptrToNeighb))
            {
                // сравнение путей нынешнего и через cur
                if (curNeighb.ptrToNeighb->g > cur->g + curNeighb.lenBeetwen)
                {
                    // меняем родителя, если через cur выгоднее
                    curNeighb.ptrToNeighb->mother = cur;
                    // меняем значение g()
                    curNeighb.ptrToNeighb->g = cur->g + curNeighb.lenBeetwen;
                }
            }

            // условие на игнорирование вершин, находящихся в закрытом списке.
            else if (!isInList(&closedList, curNeighb.ptrToNeighb))
            {
                // определяет cur как родителя для обрабатываемого соседа
                curNeighb.ptrToNeighb->mother = cur;
                openedList.push_back(curNeighb.ptrToNeighb); // записывает соседа в открытый список
                curNeighb.ptrToNeighb->g = cur->g + curNeighb.lenBeetwen; // вычисление g() соседа
            }
        }

        // проверка открытого списка. Если он пуст, то путь не существует. Вернется пустой вектор
        if (openedList.empty())
        {
            return road;
        }

        size_t maxIndex = 0; // выбор нового cur по наибольшему f() в открытом списке
        // цикл поиска индекса элемента в открытом списке с наибольшим f()
        for (int i = 1; i < openedList.size(); ++i)
        {
            if (openedList[i]->f() < openedList[maxIndex]->f())
            {
                maxIndex = i;
            }
        }
        cur = openedList[maxIndex];                      // смена текущего
        // удаление нового текущего из открытого списка
        openedList.erase(openedList.begin() + maxIndex);
        closedList.push_back(cur);                       // добавление его в закрытый список

        if (cur == end) // проверка на совпадение с целевой вершиной
        {
            Dot *motherIterator = cur;       // переменная для обхода по родителям
            road.push_back(motherIterator);  // записывавет найденную целевую вершину в вектор пути
            while (motherIterator != start) // цикл обхода родителей и записи их в вектор пути
            {
                motherIterator = motherIterator->mother;
                road.insert(road.begin(), motherIterator);
            }
        }
    }
    return road; // возврат пути
}

int main()
{
    int n, h, m, k, d;
    cin >> n;
    vector<Dot*> v;;
    for (int i = 0; i < n; ++i)
    {
        Dot* node = new Dot();
        v.push_back(node);
    }

    for (int i = 0; i < n; ++i)
    {
        cin >> h;
        v[i]->h = h;
        cin >> m;
        for (int j = 0; j < m; ++j)
        {
            cin >> k >> d;
            NeighbourDot p;
            p.ptrToNeighb = v[k];
            p.lenBeetwen = d;
            v[i]->neighbours.push_back(p);
        }
    }

    vector<Dot*> road = aStar(v[0], v[n-1]);

    for (auto i: road)
        for(int j = 0; j < n; ++j)
            if (i == v[j])
            {
                cout << j << " ";
                break;
            }

    return 0;
}
