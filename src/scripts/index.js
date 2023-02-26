let submitGrades = () => {
  let students = ["A", "B", "C"];

  for (let i of students) {
    let final = 0
    for (let j = 0; j < 4; j++) {
      let id = "grade" + i + j;
      console.log(document.getElementById(id).value)
      final += parseInt(document.getElementById(id).value);
    } 
    console.log(final)
    document.getElementById("final" + i).innerText = final/4
  }
}
