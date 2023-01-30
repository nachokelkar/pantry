const groceryList = document.getElementById("grocery-list");
const itemInput = document.getElementById("item-input");
const addItemButton = document.getElementById("add-item-button");

// Fetch initial grocery list
updateGroceryList();

// Add event listeners
addItemButton.addEventListener("click", addItem);

// Fetch updated grocery list and render
async function updateGroceryList() {
  const response = await fetch("/grocery-list/get");
  const items = await response.json();
  renderGroceryList(items);
}

// Render grocery list
function renderGroceryList(items) {
  groceryList.innerHTML = "";
  items.forEach(item => {
    const li = document.createElement("li");
    li.classList.add("grocery-item");
    li.innerHTML = `
      <input type="checkbox">
      ${item}
      <button class="remove-item-button">x</button>
    `;
    li.querySelector("input[type='checkbox']").addEventListener("click", () => removeItem(item));
    li.querySelector(".remove-item-button").addEventListener("click", () => removeItem(item));
    groceryList.appendChild(li);
  });
}

// Add item to grocery list
async function addItem() {
  const item = itemInput.value;
  itemInput.value = "";
  const response = await fetch("/grocery-list/update", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ item })
  });
  updateGroceryList();
}

// Remove item from grocery list
async function removeItem(item) {
    const response = await fetch("/grocery-list/remove", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ item })
    });
    updateGroceryList();
  }
  