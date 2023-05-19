import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Run {
    public static void main(String[] args) throws IOException {
        DataProcessing dp = new DataProcessing("lake-data.csv");

        dp.generateNewFileData();
    }
}
