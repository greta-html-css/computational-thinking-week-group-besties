
import java.nio.file.{Files, Paths}
import scala.util.Try

object Main {
  def main(args: Array[String]): Unit = {
    val filePath = "/Users/gretapfeiffer/Desktop/computational-thinking-week-group-besties/challenge_day4/testdata/data6.txt"
    val lines = scala.io.Source.fromFile(filePath).getLines().toList

    val outputLines = lines.zipWithIndex.map {
      case (line, 0) => s"$line,Comments" // Add header
      case (line, _) =>
        val parts = line.split(",")
        if (parts.length < 9) {
          println(s"Skipping line due to insufficient fields. Found ${parts.length}")
          line
        } else {
          val summary = parts(7).trim.toLowerCase
          val evaluationOpt = Try(parts(8).toFloat).toOption
          println(s"Summary: '$summary', Evaluation raw: '${parts(8)}'")

          val comments = evaluationOpt match {
            case Some(evaluation) =>
              val comment = (summary, evaluation) match {
                case ("super", e) if e >= 3 => "Excellent"
                case ("super", _)           => "Good but inconsistent"
                case (_, e) if e >= 2       => "Promising"
                case _                      => "Needs Improvement"
              }
              println(s"Evaluation: $evaluation => Comment: $comment")
              comment
            case None =>
              println(s"Invalid float: ${parts(8)}")
              "Invalid Evaluation"
          }

          s"$line,$comments"
        }
    }

    Files.write(Paths.get("test_data7.txt"), outputLines.mkString("\n").getBytes)
  }
}
