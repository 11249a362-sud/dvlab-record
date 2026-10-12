# Load libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(RColorBrewer)

# Create student dataset
students <- data.frame(
  Student = c(
    "Alice", "Bob", "Charlie", "Diana", "Eve",
    "Frank", "Grace", "Henry", "Ivy", "Jack"
  ),
  Math = c(88, 72, 91, 65, 78, 85, 60, 95, 70, 83),
  Science = c(76, 85, 88, 70, 92, 79, 68, 90, 74, 80),
  English = c(82, 68, 75, 80, 70, 88, 72, 85, 77, 79),
  Hours = c(5.0, 4.0, 6.0, 3.0, 7.0, 5.5, 3.5, 7.0, 4.0, 5.0)
)

# Display the first six rows
print(head(students))

# Calculate average subject scores
avgs <- colMeans(students[, c("Math", "Science", "English")])

# Reshape data into long format
long_df <- pivot_longer(
  students,
  cols = c(Math, Science, English),
  names_to = "Subject",
  values_to = "Score"
)

# Preserve student order in plots
students$Student <- factor(
  students$Student,
  levels = students$Student
)

long_df$Student <- factor(
  long_df$Student,
  levels = levels(students$Student)
)

# 1. Bar chart: Average subject scores
png("bar_chart_R.png", width = 800, height = 600)

barplot(
  avgs,
  main = "Average Subject Scores",
  xlab = "Subject",
  ylab = "Average Score",
  col = c("#3498db", "#2ecc71", "#e74c3c"),
  ylim = c(0, 100),
  border = "black"
)

abline(
  h = mean(avgs),
  col = "darkgray",
  lty = 2,
  lwd = 2
)

legend(
  "topright",
  legend = paste("Overall Avg:", round(mean(avgs), 1)),
  lty = 2,
  col = "darkgray",
  bty = "n"
)

dev.off()

# 2. Line chart: Student score trends
line_chart <- ggplot(
  long_df,
  aes(x = Student, y = Score, color = Subject, group = Subject)
) +
  geom_line(linewidth = 1) +
  geom_point(size = 3) +
  labs(
    title = "Student Score Trends",
    x = "Student",
    y = "Marks",
    color = "Subject"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave(
  "line_chart_R.png",
  plot = line_chart,
  width = 8,
  height = 6,
  dpi = 100
)

# 3. Box plot: Score distribution by subject
box_chart <- ggplot(
  long_df,
  aes(x = Subject, y = Score, fill = Subject)
) +
  geom_boxplot(alpha = 0.7, outlier.color = "red") +
  geom_jitter(width = 0.2, alpha = 0.5) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Score Distribution by Subject",
    x = "Subject",
    y = "Score"
  ) +
  theme_light() +
  theme(legend.position = "none")

ggsave(
  "box_chart_R.png",
  plot = box_chart,
  width = 8,
  height = 6,
  dpi = 100
)

# 4. Histogram: Math score distribution
math_histogram <- ggplot(students, aes(x = Math)) +
  geom_histogram(
    binwidth = 8,
    fill = "#9b59b6",
    color = "black",
    alpha = 0.8
  ) +
  geom_vline(
    xintercept = mean(students$Math),
    color = "red",
    linetype = "dashed",
    linewidth = 1
  ) +
  labs(
    title = "Distribution of Math Scores",
    x = "Score",
    y = "Count"
  ) +
  theme_classic()

ggsave(
  "math_histogram_R.png",
  plot = math_histogram,
  width = 8,
  height = 6,
  dpi = 100
)

# 5. Scatter plot: Study hours vs Math score
scatter_chart <- ggplot(
  students,
  aes(x = Hours, y = Math, color = Math)
) +
  geom_point(size = 4) +
  geom_smooth(
    aes(x = Hours, y = Math),
    method = "lm",
    se = TRUE,
    color = "steelblue",
    linetype = "dashed"
  ) +
  scale_color_gradient(low = "orange", high = "darkblue") +
  labs(
    title = "Hours Studied vs Math Score",
    x = "Hours Studied",
    y = "Math Score",
    color = "Math Score"
  ) +
  theme_minimal()

ggsave(
  "study_hours_vs_math_R.png",
  plot = scatter_chart,
  width = 8,
  height = 6,
  dpi = 100
)

# 6. Grouped bar chart: Scores by student and subject
grouped_chart <- ggplot(
  long_df,
  aes(x = Student, y = Score, fill = Subject)
) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_brewer(palette = "Set1") +
  labs(
    title = "Scores by Student and Subject",
    x = "Student",
    y = "Score",
    fill = "Subject"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave(
  "grouped_bar_chart_R.png",
  plot = grouped_chart,
  width = 10,
  height = 6,
  dpi = 100
)

# 7. Pie chart: Count A-grades (score >= 85)
a_grades <- c(
  Math = sum(students$Math >= 85),
  Science = sum(students$Science >= 85),
  English = sum(students$English >= 85)
)

png("a_grade_pie_chart_R.png", width = 800, height = 600)

pie(
  a_grades,
  main = "A-Grade Distribution by Subject",
  col = c("#3498db", "#2ecc71", "#e74c3c"),
  labels = paste(
    names(a_grades),
    "\n",
    a_grades,
    "students"
  )
)

dev.off()

# Display all ggplot charts in RStudio
print(line_chart)
print(box_chart)
print(math_histogram)
print(scatter_chart)
print(grouped_chart)

# Print average scores
cat("\nAverage Subject Scores:\n")
print(round(avgs, 2))

# Print A-grade counts
cat("\nA-Grade Counts (Score >= 85):\n")
print(a_grades)

# Display the output folder
cat("\nCharts saved in:\n")
print(getwd())