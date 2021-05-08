<template>
  <div>
    <StartPage
      v-if="currentPage === 'start'"
      v-on:file-loaded="onFileLoaded"
      v-on:classification-page="renderClassificationpage"
      v-on:generation-page="renderGenerationpage"
    />
    <AnnotationPage v-if="currentPage === 'annotator'" />
    <TextClassificationPage v-if="currentPage === 'classification'" />
    <SequenceGenerationPage v-if="currentPage === 'generation'" />
  </div>
</template>

<script>
import StartPage from "./components/StartPage";
import AnnotationPage from "./components/AnnotationPage";
import TextClassificationPage from "./components/TextClassificationPage";
import SequenceGenerationPage from "./components/SequenceGenerationPage";

import "./assets/styles.scss";

export default {
  name: "App",
  data: function () {
    return {
      currentPage: "start",
    };
  },
  components: {
    StartPage,
    AnnotationPage,
    TextClassificationPage,
    SequenceGenerationPage,
  },
  methods: {
    onFileLoaded() {
      this.currentPage = "annotator";
    },
    renderHomePage() {
      this.currentPage = "start";
    },

    renderClassificationpage() {
      this.currentPage = "classification";
    },

    renderGenerationpage() {
      this.currentPage = "generation";
    },
  },
  computed: {
    getCurrentPage() {
      return this.$store.state.currentPage;
    },
  },
  watch: {
    getCurrentPage(val) {
      this.currentPage = val;
    },
    currentPage(val) {
      this.$store.commit("setCurrentPage", val);
    },
  },
};
</script>
