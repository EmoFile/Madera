package me.nassim.androidApp

import android.content.Context
import android.text.Layout
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.ViewGroup.LayoutParams.*
import android.widget.BaseAdapter
import android.widget.ListView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class RangeAdapter (private val context: Context, private val list: ArrayList<Range>): BaseAdapter() {
    override fun getCount(): Int {
        return list.size
    }

    override fun getItem(p0: Int): Any {
        return list[p0]
    }

    override fun getItemId(p0: Int): Long {
        return p0.toLong()
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View = LayoutInflater.from(context).inflate(R.layout.item_range_vertical, parent, false)

        val rangeName = view.findViewById<TextView>(R.id.range_name)
        rangeName.text = list[position].name.toString()

        val moduleRecyclerView = view.findViewById<ListView>(R.id.module_item_view)
        var adapter = ModuleAdapter(view.context, list[position].module)
        adapter.notifyDataSetChanged()
        moduleRecyclerView.adapter = adapter

        return view
    }


}