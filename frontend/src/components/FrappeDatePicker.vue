<template>
	<div class="relative w-full" ref="pickerRef">
		<!-- Input Trigger -->
		<div
			class="relative flex items-center rounded-xl border border-gray-200 bg-white transition shadow-sm focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15"
			:class="{ 'border-emerald-700 ring-2 ring-emerald-700/15': isOpen }"
		>
			<!-- Calendar Icon (Frappe Style) -->
			<button
				type="button"
				@click="toggleOpen"
				tabindex="-1"
				class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-gray-400 hover:text-emerald-700 transition cursor-pointer"
				title="Open calendar"
			>
				<svg
					class="w-4 h-4"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
				>
					<rect width="18" height="18" x="3" y="4" rx="2" />
					<line x1="16" y1="2" x2="16" y2="6" />
					<line x1="8" y1="2" x2="8" y2="6" />
					<line x1="3" y1="10" x2="21" y2="10" />
				</svg>
			</button>

			<!-- Date Input Display / Entry -->
			<input
				type="text"
				:value="modelValue"
				@input="onInput"
				@focus="openCalendar"
				@keydown.esc="closeCalendar"
				:placeholder="placeholder || 'YYYY-MM-DD'"
				:required="required"
				maxlength="10"
				class="block w-full pl-10 pr-9 py-2 text-xs lg:text-sm text-gray-900 placeholder-gray-400 bg-transparent rounded-xl focus:outline-none cursor-pointer"
			/>

			<!-- Clear or Dropdown Chevron -->
			<div class="absolute inset-y-0 right-0 pr-3 flex items-center">
				<button
					v-if="modelValue"
					type="button"
					@click.stop="clearDate"
					tabindex="-1"
					class="text-gray-400 hover:text-red-500 transition p-0.5"
					title="Clear date"
				>
					<svg
						class="w-3.5 h-3.5"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<line x1="18" y1="6" x2="6" y2="18" />
						<line x1="6" y1="6" x2="18" y2="18" />
					</svg>
				</button>
				<button
					v-else
					type="button"
					@click="toggleOpen"
					tabindex="-1"
					class="text-gray-400 hover:text-gray-600 transition"
				>
					<svg
						class="w-3.5 h-3.5"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<polyline points="6 9 12 15 18 9" />
					</svg>
				</button>
			</div>
		</div>

		<!-- Frappe Calendar Popover -->
		<div
			v-if="isOpen"
			class="absolute right-0 sm:right-0 top-full mt-1.5 z-50 w-72 rounded-2xl bg-white p-3.5 shadow-2xl ring-1 ring-black/10 border border-gray-100 select-none animate-in fade-in zoom-in-95 duration-100"
		>
			<!-- Header: Month & Year Selector with Chevrons -->
			<div class="flex items-center justify-between pb-2.5 mb-2.5 border-b border-gray-100">
				<button
					type="button"
					@click="prevMonth"
					class="h-7 w-7 rounded-lg flex items-center justify-center text-gray-500 hover:text-gray-800 hover:bg-gray-100 transition"
					title="Previous Month"
				>
					<svg
						class="w-4 h-4"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<polyline points="15 18 9 12 15 6" />
					</svg>
				</button>

				<!-- Month & Year Controls -->
				<div class="flex items-center gap-1.5">
					<select
						v-model="viewMonth"
						class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-50 hover:bg-gray-100 border border-gray-200 rounded-lg cursor-pointer focus:outline-none focus:border-emerald-700"
					>
						<option v-for="(mName, mIdx) in monthNames" :key="mIdx" :value="mIdx">
							{{ mName }}
						</option>
					</select>

					<select
						v-model="viewYear"
						class="px-2 py-1 text-xs font-semibold text-gray-800 bg-gray-50 hover:bg-gray-100 border border-gray-200 rounded-lg cursor-pointer focus:outline-none focus:border-emerald-700"
					>
						<option v-for="y in yearOptions" :key="y" :value="y">
							{{ y }}
						</option>
					</select>
				</div>

				<button
					type="button"
					@click="nextMonth"
					class="h-7 w-7 rounded-lg flex items-center justify-center text-gray-500 hover:text-gray-800 hover:bg-gray-100 transition"
					title="Next Month"
				>
					<svg
						class="w-4 h-4"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<polyline points="9 18 15 12 9 6" />
					</svg>
				</button>
			</div>

			<!-- Days of Week Header -->
			<div class="grid grid-cols-7 gap-1 text-center mb-1">
				<div
					v-for="d in ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']"
					:key="d"
					class="text-[10px] font-bold text-gray-400 uppercase tracking-wider py-0.5"
				>
					{{ d }}
				</div>
			</div>

			<!-- Calendar Days Grid -->
			<div class="grid grid-cols-7 gap-1">
				<button
					v-for="(cell, i) in calendarCells"
					:key="i"
					type="button"
					@click="selectCell(cell)"
					:class="[
						'h-7 w-7 sm:h-8 sm:w-8 mx-auto flex items-center justify-center rounded-lg text-xs transition',
						cell.isSelected
							? 'bg-emerald-700 text-white font-bold shadow-sm shadow-emerald-700/30'
							: cell.isToday
							? 'text-emerald-700 font-bold border border-emerald-600/40 hover:bg-emerald-50'
							: cell.isCurrentMonth
							? 'text-gray-800 font-medium hover:bg-emerald-50 hover:text-emerald-700'
							: 'text-gray-300 hover:bg-gray-50 hover:text-gray-500',
					]"
				>
					{{ cell.day }}
				</button>
			</div>

			<!-- Footer: Frappe Actions (Today & Clear) -->
			<div
				class="flex items-center justify-between pt-2.5 mt-2.5 border-t border-gray-100 text-xs"
			>
				<button
					type="button"
					@click="clearDate"
					class="px-2 py-1 text-gray-500 hover:text-red-600 font-medium transition rounded-md hover:bg-red-50"
				>
					Clear
				</button>

				<button
					type="button"
					@click="selectToday"
					class="px-2 py-1 text-emerald-700 hover:text-emerald-800 font-semibold transition rounded-md hover:bg-emerald-50"
				>
					Today
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, ref, watch } from "vue";

const props = defineProps({
	modelValue: {
		type: String,
		default: "",
	},
	placeholder: {
		type: String,
		default: "YYYY-MM-DD",
	},
	required: {
		type: Boolean,
		default: false,
	},
});

const emit = defineEmits(["update:modelValue", "change"]);

const pickerRef = ref(null);
const isOpen = ref(false);

const monthNames = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December",
];

// Determine current year and bounds
const currentYearNow = new Date().getFullYear();
// Generate year options from currentYear downto 1930
const yearOptions = computed(() => {
	const years = [];
	for (let y = currentYearNow; y >= 1930; y--) {
		years.push(y);
	}
	return years;
});

// View navigation state
const viewYear = ref(currentYearNow);
const viewMonth = ref(new Date().getMonth());

function syncWithModel(val) {
	if (val && /^\d{4}-\d{2}-\d{2}$/.test(val)) {
		const [y, m] = val.split("-").map(Number);
		if (!isNaN(y) && !isNaN(m)) {
			viewYear.value = y;
			viewMonth.value = m - 1;
		}
	}
}

watch(
	() => props.modelValue,
	(newVal) => {
		syncWithModel(newVal);
	},
	{ immediate: true }
);

function toggleOpen() {
	isOpen.value ? closeCalendar() : openCalendar();
}

function openCalendar() {
	if (!isOpen.value) {
		if (props.modelValue) {
			syncWithModel(props.modelValue);
		} else {
			// Default to 18-20 years ago if empty for convenient Date of Birth selection
			const defaultYear = currentYearNow - 18;
			viewYear.value = defaultYear;
			viewMonth.value = new Date().getMonth();
		}
		isOpen.value = true;
	}
}

function closeCalendar() {
	isOpen.value = false;
}

function prevMonth() {
	if (viewMonth.value === 0) {
		viewMonth.value = 11;
		viewYear.value--;
	} else {
		viewMonth.value--;
	}
}

function nextMonth() {
	if (viewMonth.value === 11) {
		viewMonth.value = 0;
		viewYear.value++;
	} else {
		viewMonth.value++;
	}
}

// Compute calendar day cells
const calendarCells = computed(() => {
	const cells = [];
	const year = viewYear.value;
	const month = viewMonth.value;

	const firstDayIndex = new Date(year, month, 1).getDay(); // 0 is Sunday
	const daysInMonth = new Date(year, month + 1, 0).getDate();
	const daysInPrevMonth = new Date(year, month, 0).getDate();

	const todayStr = formatYMD(new Date());
	const selectedStr = props.modelValue;

	// Previous month padding
	for (let i = firstDayIndex - 1; i >= 0; i--) {
		const day = daysInPrevMonth - i;
		const prevMonthDate = new Date(year, month - 1, day);
		const dateStr = formatYMD(prevMonthDate);
		cells.push({
			day,
			date: prevMonthDate,
			dateStr,
			isCurrentMonth: false,
			isToday: dateStr === todayStr,
			isSelected: dateStr === selectedStr,
		});
	}

	// Current month days
	for (let day = 1; day <= daysInMonth; day++) {
		const curDate = new Date(year, month, day);
		const dateStr = formatYMD(curDate);
		cells.push({
			day,
			date: curDate,
			dateStr,
			isCurrentMonth: true,
			isToday: dateStr === todayStr,
			isSelected: dateStr === selectedStr,
		});
	}

	// Next month padding to fill standard 42 cells (6 rows) or minimum 35 cells
	const remaining = cells.length % 7 === 0 ? 0 : 7 - (cells.length % 7);
	for (let day = 1; day <= remaining; day++) {
		const nextMonthDate = new Date(year, month + 1, day);
		const dateStr = formatYMD(nextMonthDate);
		cells.push({
			day,
			date: nextMonthDate,
			dateStr,
			isCurrentMonth: false,
			isToday: dateStr === todayStr,
			isSelected: dateStr === selectedStr,
		});
	}

	return cells;
});

function formatYMD(date) {
	const y = date.getFullYear();
	const m = String(date.getMonth() + 1).padStart(2, "0");
	const d = String(date.getDate()).padStart(2, "0");
	return `${y}-${m}-${d}`;
}

function selectCell(cell) {
	emit("update:modelValue", cell.dateStr);
	emit("change", cell.dateStr);
	closeCalendar();
}

function selectToday() {
	const todayStr = formatYMD(new Date());
	emit("update:modelValue", todayStr);
	emit("change", todayStr);
	closeCalendar();
}

function clearDate() {
	emit("update:modelValue", "");
	emit("change", "");
	closeCalendar();
}

function onInput(e) {
	const val = e.target.value.trim();
	emit("update:modelValue", val);
	emit("change", val);
}

// Click outside handler
function handleClickOutside(e) {
	if (pickerRef.value && !pickerRef.value.contains(e.target)) {
		closeCalendar();
	}
}

onMounted(() => {
	document.addEventListener("click", handleClickOutside);
});

onUnmounted(() => {
	document.removeEventListener("click", handleClickOutside);
});
</script>
