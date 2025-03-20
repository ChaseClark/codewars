// See https://aka.ms/new-console-template for more information
using System.Data;
using System.Runtime.CompilerServices;
using System.Text;

Console.WriteLine("Test");

// create an alorithim that traverses a 2d string[] array, * chars are the path and save every actual letter
// to build into a word. stop when there is no more path to traverse
// height = 10
// width = 15

int height = 10;
int width = 15;
var gridMap = new List<string[]>();

gridMap.Add(new string[15] { "*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", "h", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", "e", "*", "l", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", " ", " ", "l", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", " ", " ", "o", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });
gridMap.Add(new string[15] { " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " });


foreach (var row in gridMap)
{
    Console.WriteLine(String.Join("", row));
    foreach (var col in row)
    {
        //Console.WriteLine(col);
    }
}

//for (int i = 0; i < width; i++)
//{
//    // check 0,0

//}

bool done = false;
int x = 0, y = 0;
int prevX = 0, prevY = 0;
var sb = new StringBuilder();
while (!done)
{
    // check current position
    var current = gridMap[x][y];
    // check U D L R for next char
    int up = y - 1;
    int down = y + 1;
    int left = x - 1;
    int right = x + 1;
    Console.WriteLine($"current <{current}> x{x} y{y} prevX{prevX} prevy{prevY} up{up} down{down} left{left} right{right}");
    if (prevY != up && up >= 0 && gridMap[up][x] != " ") // up
    {
        if (gridMap[up][x] != "*")
        {
            sb.Append(gridMap[up][x]);
            Console.WriteLine($"Appending right {gridMap[up][x]}");
        }
        prevY = y;
        y = up;
    }
    else if (prevY != right && right < width && gridMap[y][right] != " ") // right
    {
        if (gridMap[y][right] != "*")
        {
            sb.Append(gridMap[y][right]);
            Console.WriteLine($"Appending right {gridMap[y][right]}");
        }
        prevX = x;
        x = right;
    }
    else if (prevY != down && down < height && gridMap[down][x] != " ") // down
    {
        if (gridMap[down][x] != "*")
        {
            sb.Append(gridMap[down][x]);
            Console.WriteLine($"Appending right {gridMap[down][x]}");
        }
        prevY = y;
        y = down;
    }
    else if (prevY != left && left >= 0 && gridMap[y][left] != " ") // left
    {
        if (gridMap[y][left] != "*")
        {
            sb.Append(gridMap[y][left]);
            Console.WriteLine($"Appending right {gridMap[y][left]}");
        }
        prevX = x;
        x = left;
    }
    else
    {
        done = true;
    }
}

Console.WriteLine($" ans:{sb}");
Console.ReadLine();