package templates;

import java.util.HashMap;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.function.Function;

public class Evaluator {

    public BiFunction<Boolean, Boolean, Boolean> xor_gate() {
        // TODO BY STUDENT
        @   @student_gate_xor@@
    }

    public BiFunction<Boolean, Boolean, Boolean> or_gate() {
        // TODO BY STUDENT
        @   @student_gate_or@@
    }

    public BiFunction<Boolean, Boolean, Boolean> and_gate() {
        // TODO BY STUDENT
        @   @student_gate_and@@
    }

    public Function<Boolean, Boolean> not_gate() {
        // TODO BY STUDENT
        @   @student_gate_not@@
    }

    // Should return a map with the results stored in map ( use HashMap )
    // Keys are "SUM", "CarryOut"
    // WARNING : USE HERE ONLY the previously defined method to compute result (as inginious will prevent you to cheat to directly invoke logical operators)
    public Map<String, Boolean> evaluate_circuit(Boolean a, Boolean b, Boolean carry_in) {
        // TODO BY STUDENT
        @   @student_evaluate@@
    }

}