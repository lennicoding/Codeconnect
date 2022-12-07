function next() {
  let title = document.getElementById("title");
  if (title.value == "" || title.value == " ") {
    alert("Please fill out the title field");
  } else {
    const titleValue = title.value;
    localStorage.setItem("title", titleValue);
    link();
  }
}

function next_description() {
  let description = document.getElementById("description");
  const title = localStorage.getItem("title");

  if (description.value == "" || description.value == " ") {
    alert("Please fill out the description field");
  } else {
    const descriptionValue = description.value;
    localStorage.setItem("description", descriptionValue);
    link_description();
  }
}

function next_tags() {
  var tags = "";
  var title = localStorage.getItem("title");
  var description = localStorage.getItem("description");
  var checkedBoxes = document.querySelectorAll(
    "input[name=checkboxes]:checked"
  );
  for (var i = 0; i < checkedBoxes.length; i++) {
    tags += checkedBoxes[i].value + ",";
  }
    sendToBackend(title, description, tags);
    link_tags();
}
