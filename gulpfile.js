const gulp = require('gulp');
const browserSync = require('browser-sync');
const modifyCssUrls = require('gulp-modify-css-urls');
const sass = require('gulp-sass');
const rename = require('gulp-rename');

function swallowError(error) {
  console.error(error.toString());
  this.emit('end')
}

gulp.task('default', ['sass'], function () {
  browserSync.init({
    notify: false,
    proxy: "localhost:9000"
  });
  gulp.watch("apps/main/static/css/*.scss", ['sass'])
});

gulp.task('sass', function () {
  return gulp.src("apps/main/static/css/*.scss")
    .pipe(sass()).on('error', swallowError)
    .pipe(modifyCssUrls({
      modify(url, filePath) {
        return url.replace('..', '/static')
      }
    }))
    .pipe(rename({suffix: '.compiled'}))
    .pipe(gulp.dest("static/CACHE/css"))
    .pipe(browserSync.stream())
});

gulp.task('build', ['prod']);

gulp.task('prod', ['sass'], function () {
//    TODO: Add minification
});
