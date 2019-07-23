import java.util.stream.Stream;

public interface StudentStreamFunction {

    // Find the N°2 and N°3 top students for the given course name in parameter
    public Stream<Student> find_second_and_third_top_student_for_given_course(Stream<Student> studentStream,
                                                                              String name);

    // Compute for each student in the given section their average grade result,
    // sorted by their result (ascending) as an array of array structured like that :
    // [ [ "Student FirstName1 LastName1", 7.5 ], [ "Student FirstName2 LastName2", 9.5 ]  ]
    public Object[] compute_average_for_student_in_section(Stream<Student> studentStream,
                                                           int section);

    // Give the number of students that success in all courses (> 10.0)
    public int get_number_of_successful_students(Stream<Student> studentStream);

    // Find the student that is the last one in the lexicographic order
    // ( You must first compare students on their lastNames then on their firstNames )
    public Student find_last_in_lexicographic_order(Stream<Student> studentStream);


    // Give the full sum of the grade obtained by all students
    public double get_full_sum(Stream<Student> studentStream);

}