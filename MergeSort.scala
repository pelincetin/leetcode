object MergeSort {

    def merge(list1 : List[Int], list2 : List[Int]) : List[Int] = (list1, list2) match{
        // write this method
      case (list1, Nil) => list1
      case (Nil, list2) => list2
      case (list1head :: list1tail, list2head :: list2tail) =>
        if (list2head < list1head)
          list2head :: merge(list1, list2tail)
        else
          list1head :: merge(list1tail, list2)

    }

    def sort(list : List[Int]) : List[Int] = {
        // write this method
        val split_index = list.length/2
        if (list.length < 2)
            list
        else{
            val(left, right) = list.splitAt(split_index)
            merge(sort(left), sort(right))
        }
    }

    def main(args : Array[String]) {
        println(sort(List(9,5,7,3,1,4,6,2,8,0)));
    }
}

