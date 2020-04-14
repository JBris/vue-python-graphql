<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title" @click="isCollapsed = !isCollapsed">{{title}}</p>
    </header>
    <div class="card-content" :class="{'is-hidden':isCollapsed }">
      <slot v-if="!isCollapsed"></slot>
    </div>
    <footer class="card-footer" v-if="!isCollapsed">
      <slot name="footer"></slot>
    </footer>
  </div>
</template>

<script>
export default {
  mounted() {
    if (this.id) {
      const state = this.getCollapseState();
      if (state) {
        this.isCollapsed = state[this.id];
      }
    }
  },
  props: {
    id: {
      type: String
    },
    title: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      isCollapsed: true
    };
  },
  methods: {
    getCollapseState() {
      return localStorage.getObject("collapsibles") || {};
    },
    saveCollapsedState(value) {
      const state = this.getCollapseState();
      state[this.id] = value;
      localStorage.setObject("collapsibles", state);
    }
  },
  watch: {
    isCollapsed(newValue) {
      if (this.id) {
        this.saveCollapsedState(newValue);
      }
      this.$emit("collapseChanged", newValue);
    }
  }
};
</script>

<style scoped lang="scss">
$turquoise: hsl(171, 100%, 41%);

.card-header {
  box-shadow: 0px 0px 0px 8px rgba(0,0,0,0); 
}
.card-header-title{
  text-align: left;
  text-decoration: underline;
  font-weight: bold;
}
.card {
  margin: 0.05rem;
  width: 200%;
  box-shadow: 0.10em 0.10em 5px grey;
  border-radius: 1.5em;
  border: 0.05em solid $turquoise;
}
.card-content {
  text-align: left
}
</style>
