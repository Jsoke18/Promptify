document.addEventListener('DOMContentLoaded', () => {
    async function fetchTags() {
      const response = await fetch("/tags");
      const tags = await response.json();
      const tagFilter = document.getElementById("tag_filter");
      tags.forEach((tag) => {
        const option = document.createElement("option");
        option.value = tag;
        option.textContent = tag;
        tagFilter.appendChild(option);
      });
    }
    fetchTags();
  });
  