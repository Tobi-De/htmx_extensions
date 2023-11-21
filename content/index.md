<figure>
<table role="grid">
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Description</th>
      <th scope="col">Repository</th>
      <th scope="col">Official</th>
    <th scope="col">Download</th>
    </tr>
  </thead>
  <tbody>
  {% for name, ext in data.extensions.items %}
    <tr>
      <td scope="row">{{name}}</t>
      <td scope="row">{{ext.description}}</td>
      <td scope="row"><a href="{{ext.repo_url}}">{{ext.repo_url}}</a></td>
      <td scope="row">
      {% if ext.is_official is True %}
        <div class="pos">
            <img src="{% static 'svg/check.svg' %}">
        </div>
        {% elif ext.is_official is False %}
        <div class="neg">
            <img src="{% static 'svg/x.svg' %}">
        </div>
        {% endif %}
      </td>
      <td scope="row">
         <a href="{{ext.download_url}}" role="button" class="outline" download>Download</a>
      </td>
    </tr>
  {% endfor %}
  </tbody>
  <tfoot>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Description</th>
      <th scope="col">Repository</th>
      <th scope="col">Official</th>
    <th scope="col">Download</th>
    </tr>
  </tfoot>
</table>
</figure>