<script>
  window.onload = function() {
    const ui = SwaggerUIBundle({
      url: "path/to/your/swagger.json",
      dom_id: '#swagger-ui',
      presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIStandalonePreset
      ],
      plugins: [
        // Add custom plugins here
      ],
      layout: "BaseLayout"
    });

    // Custom JavaScript code
    document.querySelector('.topbar').style.backgroundColor = '#123456';
  }
</script>
