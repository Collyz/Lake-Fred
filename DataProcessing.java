import java.io.*;
import java.util.ArrayList;

public class DataProcessing {
    private BufferedReader br;
    private BufferedWriter bw;
    private ArrayList<Integer> xValues;
    private ArrayList<Integer> yValues;

    /**
     * Constructor that accepts a filename
     * @param filename - The name of the file
     * @throws FileNotFoundException - Exception if file not found
     */
    public DataProcessing(String filename) throws FileNotFoundException {
        br = new BufferedReader(new FileReader(filename));
        xValues = new ArrayList<>();
        yValues = new ArrayList<>();
    }

    /**
     * Helper method that gets all x values in the data set
     */
    public void getValues()throws IOException{
        String temp;
        while((temp = br.readLine()) != null){
            String[] values = temp.split(",");
            xValues.add(Integer.parseInt(values[0]));
            yValues.add(Integer.parseInt(values[1]));
        }
    }

    /**
     * Finds the smallest x in the data
     * @return Returns the smallest x value in the data
     * @throws IOException If the file cannot be found
     */
    public int findMinimumX() throws IOException {
        int min = Integer.MAX_VALUE;
        for (Integer xValue : xValues) {
            if (xValue < min) {
                min = xValue;
            }
        }
        return min;
    }

    /**
     * Finds the smallest y in the data
     * @return Returns the smallest y value in the data
     * @throws IOException If the file cannot be found
     */
    public int findMinimumY() throws IOException {
        int min = Integer.MAX_VALUE;
        for (Integer yValue : yValues) {
            if (yValue < min) {
                min = yValue;
            }
        }
        return min;
    }

    /**
     * Subtracts the smallest x value from all x values
     * @return An array list of the minimized x values
     * @throws IOException Error if the file cannot be read from
     */
    public ArrayList<Integer> xMinimizedValues() throws IOException {
        int minX = findMinimumX();
        ArrayList<Integer> xMinimizedValues = this.xValues;
        for(int i = 0; i < xValues.size(); i++){
            xMinimizedValues.set(i, xValues.get(i)-minX);
        }
        return xMinimizedValues;
    }

    /**
     * Subtracts the smallest y value from all y values
     * @return An array list of the minimized y values
     * @throws IOException Error if the file cannot be read from
     */
    public ArrayList<Integer> yMinimizedValues() throws IOException {
        int minY = findMinimumY();
        ArrayList<Integer> yMinimizedValues = this.yValues;
        for(int i = 0; i < yValues.size(); i++){
            yMinimizedValues.set(i, yValues.get(i)-minY);
        }
        return yMinimizedValues;
    }

    public void generateNewFileData() throws IOException {
        File file = new File("data.csv");
        bw = new BufferedWriter(new FileWriter(file));
        getValues();
        ArrayList<Integer> xValues = xMinimizedValues();
        ArrayList<Integer> yValues = yMinimizedValues();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < xValues.size(); i++){
            sb.append(xValues.get(i));
            sb.append(",");
            sb.append(yValues.get(i));
            sb.append("\n");
        }
        bw.write(sb.toString());
        bw.close();
    }
}
