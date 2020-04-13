<template>
    <div class="panel panel-default">
        <div class="panel-heading">
            <p>{{ repo.repo }}</p>
            <p>{{ repo.author }}</p>
        </div>
        <div class="panel-body">
            <p>{{ repo.htmlUrl }}</p>
            <p>{{ repo.description }}</p>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'ListItem',
    props:{
      repo:{
        type : Object,
        required:true
      },
    }
  };
</script>