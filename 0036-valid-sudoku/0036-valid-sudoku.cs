public class Solution
{
    public bool IsValidSudoku(char[][] board)
    {
        int rows = board.Length;
        int cols = board[0].Length;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (board[i][j] == '.')
                {
                    continue;
                }

                // Check row
                for (int x = 0; x < cols; x++)
                {
                    if (x == j)
                    {
                        continue;
                    }

                    if (board[i][x] == board[i][j])
                    {
                        return false;
                    }
                }

                // Check column
                for (int y = 0; y < rows; y++)
                {
                    if (y == i)
                    {
                        continue;
                    }

                    if (board[y][j] == board[i][j])
                    {
                        return false;
                    }
                }

                // Find start of current 3x3 box
                int rowStart = i - i % 3;
                int colStart = j - j % 3;

                // Check 3x3 box
                for (int row = rowStart; row < rowStart + 3; row++)
                {
                    for (int col = colStart; col < colStart + 3; col++)
                    {
                        if (row == i && col == j)
                        {
                            continue;
                        }

                        if (board[row][col] == board[i][j])
                        {
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
}