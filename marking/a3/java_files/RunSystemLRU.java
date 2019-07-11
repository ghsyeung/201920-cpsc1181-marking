import java.util.ArrayList;

public class RunSystemLRU {
    public static void main(String[] args) {
        int maxMemory = Integer.parseInt(args[0]);

        ArrayList<App> activeAppList = new ArrayList<App>();

        LeastRecentlyUsedStrategy lruStrategy = new LeastRecentlyUsedStrategy(maxMemory, activeAppList);

        SimulatedSystem simulatedSystem = new SimulatedSystem(lruStrategy, activeAppList);

        UserInput userInput = new UserInput(simulatedSystem);

        userInput.run();
    }
}
