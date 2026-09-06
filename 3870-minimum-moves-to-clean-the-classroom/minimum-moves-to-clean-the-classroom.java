import java.util.*;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();

        int sr = 0, sc = 0;
        int litterCount = 0;

        int[][] litterId = new int[m][n];

        for (int i = 0; i < m; i++) {
            Arrays.fill(litterId[i], -1);
        }

        // Find starting position and number the litter cells
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char c = classroom[i].charAt(j);

                if (c == 'S') {
                    sr = i;
                    sc = j;
                } else if (c == 'L') {
                    litterId[i][j] = litterCount++;
                }
            }
        }

        int allCollected = (1 << litterCount) - 1;

        Queue<State> queue = new LinkedList<>();

        boolean[][][][] visited =
            new boolean[m][n][energy + 1][1 << litterCount];

        queue.offer(new State(sr, sc, energy, 0));
        visited[sr][sc][energy][0] = true;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        int moves = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            while (size-- > 0) {
                State cur = queue.poll();

                // All litter collected
                if (cur.mask == allCollected) {
                    return moves;
                }

                for (int d = 0; d < 4; d++) {
                    int nr = cur.r + dr[d];
                    int nc = cur.c + dc[d];

                    // Boundary check
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                        continue;
                    }

                    // Obstacle
                    if (classroom[nr].charAt(nc) == 'X') {
                        continue;
                    }

                    // Cannot move if energy is 0
                    if (cur.energy == 0) {
                        continue;
                    }

                    int newEnergy = cur.energy - 1;
                    int newMask = cur.mask;

                    char cell = classroom[nr].charAt(nc);

                    // Collect litter
                    if (cell == 'L') {
                        int id = litterId[nr][nc];
                        newMask |= (1 << id);
                    }

                    // Reset energy
                    if (cell == 'R') {
                        newEnergy = energy;
                    }

                    if (!visited[nr][nc][newEnergy][newMask]) {
                        visited[nr][nc][newEnergy][newMask] = true;

                        queue.offer(
                            new State(nr, nc, newEnergy, newMask)
                        );
                    }
                }
            }

            moves++;
        }

        return -1;
    }

    static class State {
        int r;
        int c;
        int energy;
        int mask;

        State(int r, int c, int energy, int mask) {
            this.r = r;
            this.c = c;
            this.energy = energy;
            this.mask = mask;
        }
    }
}