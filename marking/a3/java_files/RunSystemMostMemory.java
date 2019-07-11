import java.util.ArrayList;

public class RunSystemMostMemory {
    public static void main(String[] args) {
        int maxMemory = Integer.parseInt(args[0]);

        ArrayList<App> activeAppList = new ArrayList<App>();

        MostMemoryFirstStrategy mostMemoryFirstStrategy = new MostMemoryFirstStrategy(maxMemory, activeAppList);

        SimulatedSystem simulatedSystem = new SimulatedSystem(mostMemoryFirstStrategy, activeAppList);

        UserInput userInput = new UserInput(simulatedSystem);

        userInput.run();
    }
}
